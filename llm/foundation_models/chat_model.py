from langchain.chat_models.openai import ChatOpenAI


def create_model():
    return ChatOpenAI(
        temperature=0,
    )