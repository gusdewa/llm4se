
def ask(query: str):
    response = f"MOCKED RESULT22: {query}"

    return response


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
