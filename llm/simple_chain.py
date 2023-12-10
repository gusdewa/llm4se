from langchain.chat_models.openai import ChatOpenAI


def invoke(query: str):
    llm = ChatOpenAI()
    response = llm.invoke(query)
    return response.content
