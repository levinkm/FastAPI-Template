from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    BackgroundTasks
)


background_tasks = BackgroundTasks()

router = APIRouter(tags=["Wallet"], prefix="/wallet")
