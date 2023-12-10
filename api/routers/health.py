from fastapi import APIRouter, Response, status
from fastapi.responses import RedirectResponse

from utils import check_db_health

health_router = APIRouter()


@health_router.get("/")
async def main():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@health_router.get("/health")
async def check_health():
    db_status = check_db_health()
    return Response(status_code=status.HTTP_200_OK, content="DB is connected") \
        if db_status is True else Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
