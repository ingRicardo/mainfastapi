from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.recursion import resfact, resfib, typerecursion
from services.arguments import  argsval, kwargsval, nonkeyargs, multiplyargs, kwargsval2, formated_kwargs, args_and_kwargs
router = APIRouter(
    prefix="/tuto",
    tags=["Tuto_4"]
)


@router.get("/tuto4")
async def tutorial_4():
    pass
    return {"resfact": resfact, "resfib": resfib, "typerecursion": typerecursion, "argsval": argsval, "kwargsval": kwargsval, "nonkeyargs": nonkeyargs, "multiplyargs": multiplyargs,
            "kwargsval2": kwargsval2, "formated_kwargs": formated_kwargs, "args_and_kwargs": args_and_kwargs}