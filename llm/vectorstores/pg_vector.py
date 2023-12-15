from langchain.vectorstores.pgvector import PGVector
from utils import generate_connection_string
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document


class PGVectorStore:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        # Check if an instance already exists
        if cls._instance is None:
            # Create a new instance if it doesn't exist
            cls._instance = super(PGVectorStore, cls).__new__(cls)
            # Initialize the instance
            cls._instance.__init_once(*args, **kwargs)
        return cls._instance

    def __init_once(self, 
                    embeddings: Embeddings,
                    collection_name: str = 'default_collection'):
        # This method will only be called once to initialize the instance
        self.vstore = PGVector(
            collection_name=collection_name,
            embedding_function=embeddings,
            connection_string=generate_connection_string()
        )
        self.embeddings = embeddings
        self.collection_name = collection_name

    def store(self, docs: list[Document]):
        try:
            self.vstore.add_documents(docs)
        except Exception as e:
            raise Exception(f"Failed to store docs: {e}") from e


    def create_retriever(self):
        return self.vstore.as_retriever()
    