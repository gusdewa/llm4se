
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import TextSplitter


def create_docs(file_path: str = "data/amazon_reviews.csv"):
    # initiate loader
    loader = CSVLoader(file_path=file_path)
    docs = loader.load()
    return docs
