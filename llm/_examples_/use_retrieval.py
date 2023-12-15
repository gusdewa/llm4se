from uuid import uuid4
from langchain.chains import ConversationalRetrievalChain

from llm.prompts.chat_prompt import create_prompt
from llm.foundation_models.chat_model import create_model
from llm.foundation_models.embedding_model import create_model as create_embeddings
from llm.memories.pg_memory import create_memory
from llm.vectorstores.pg_vector import PGVectorStore

# ask LLM with context from vectordb + history of conversation
def ask(query, 
        # pass conversation_id from FE to maintain the history of the conversation
        conversation_id: str = uuid4()):
    
    llm = create_model()
    condense_question_llm = create_model()

    # memory enables us to extend the prompt with history of our chat
    # having the same conversation_id
    memory = create_memory(conversation_id)

    # yes I know it's ton of steps
    # this enable us to use LLM to condense and embed the query
    embedding_model = create_embeddings()
    vstore = PGVectorStore(embedding_model)
    retriever = vstore.create

    # power of langchain: chain!
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever
    )

    result = chain.invoke(query)
    return result



