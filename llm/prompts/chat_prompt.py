from langchain.prompts.chat import ChatPromptTemplate

from langchain.vectorstores.pinecone import Pinecone

def create_prompt(query):
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a {adjective} AI bot. You need to reply with relevant tone."),
        ("human", "{user_input}"),
    ])

    prompt = template.format_messages(
        user_input={query},
        adjective="sarcasm"
    )

    return prompt
