# I put multiple examples in _examples_ folder
from llm._examples_.use_parser import ask as ask_with_parser

def ask(query: str):
    result = ask_with_parser(query)
    
    return result


def store_docs_to_vectordb(file_path: str = "data/amazon_reviews.csv"):
    try:
        print("Start loading documents ...")
        # load documents

        print("Splitting ...")
        # split documents

        print("Embedding ...")
        # embed documents

        print("Storing ...")
        # store documents

        print("Finished!!")
    except Exception as e:
        print(f'Error: {e}')
