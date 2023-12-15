from uuid import uuid4

from langchain.memory import ConversationBufferMemory, PostgresChatMessageHistory
from utils import generate_connection_string


def create_memory(conversation_id: str = uuid4()):
    try:
        conn_string = generate_connection_string()
        history = PostgresChatMessageHistory(
            connection_string=conn_string,
            session_id=conversation_id,
        )
    except Exception as e:
        print(f'Error in building memory: {e}')

    memory = ConversationBufferMemory(
        chat_memory=history,
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    return memory
