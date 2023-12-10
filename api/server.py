from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from api.routers.health import health_router
from api.routers.chat import chat_router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(health_router)
    app_.include_router(chat_router)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="LLM Live Coding Session",
        description="Getting fun with LLM for software engineer",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()
