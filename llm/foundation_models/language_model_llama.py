from langchain.llms.llamacpp import LlamaCpp


def create_model():
    return LlamaCpp(
        temperature=0
    )