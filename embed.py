import llm
from dotenv import load_dotenv

load_dotenv()

def embed():
    try:
        llm.store_docs_to_vectordb(
            file_path="data/amazon_reviews.csv"
        )
    except Exception as e:
        print(e)

embed()
