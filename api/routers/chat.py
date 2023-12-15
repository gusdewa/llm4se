from uuid import uuid4
from fastapi import APIRouter, Response, status
from pydantic import BaseModel
import llm

chat_router = APIRouter()

class ChatArgs(BaseModel):
    collection_name: str = 'external'
    conversation_id: str = uuid4()
    query: str = 'Halo, kamu siapa?'


@chat_router.post("/chat")
async def chat(args: ChatArgs):
    try:
        # We will be using this variable to send the response back to client app
        result = llm.ask(args.query, conversation_id=args.conversation_id)
        return Response(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=e)
