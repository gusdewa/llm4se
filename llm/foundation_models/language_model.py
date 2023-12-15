from langchain.llms.openai import OpenAI


def create_model():
    return OpenAI(
        temperature=0
    )