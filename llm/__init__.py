# I put multiple examples in _examples_ folder
from llm._examples_.use_parser import ask as ask_with_parser
from llm._examples_.use_chat import ask as ask_with_chat 
from llm._examples_.use_retrieval import ask as ask_with_retrieval 

def ask(query: str, conversation_id: str):
    # result = ask_with_chat(query) # uncomment if you don't wanna use parser
    # result = ask_with_retrieval(query, conversation_id) # make sure you have embedded the docs into vector DB
    
    # example: who is president of indonesia?
    result = ask_with_parser(query)
    return result


from llm.documents.amazon_reviews import create_docs
from llm.vectorstores.pg_vector import PGVectorStore
from llm.foundation_models.embedding_model import create_model

def store_docs_to_vectordb(file_path: str = "data/amazon_reviews.csv"):
    try:
        print("Start loading documents ...")
        docs = create_docs(file_path)
        
        print("Embedding & storing")
        embedding_model = create_model()
        vstore = PGVectorStore(embedding_model)

        # this will take sametime
        vstore.store(docs)
    except Exception as e:
        print(f'Error: {e}')


 #OperationalError('could not translate host name "0.0.0.0 # this is used for local development" to address: nodename nor servname provided, or not known\n')