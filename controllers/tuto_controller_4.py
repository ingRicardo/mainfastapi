from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.recursion import resfact, resfib, typerecursion

router = APIRouter(
    prefix="/tuto",
    tags=["Tuto_4"]
)


@router.get("/tuto4")
async def tutorial_4():
    pass
    return {"resfact": resfact, "resfib": resfib, "typerecursion": typerecursion}