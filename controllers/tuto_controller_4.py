from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.recursion import resfact, resfib, typerecursion
from services.arguments import  argsval, kwargsval, nonkeyargs, multiplyargs, kwargsval2, formated_kwargs, args_and_kwargs
from services.firstclassfunc import f, fun1, msg, funcres, d
router = APIRouter(
    prefix="/tuto",
    tags=["Tuto_4"]
)


@router.get("/tuto4")
async def tutorial_4():
    pass
    return {"resfact": resfact, "resfib": resfib, "typerecursion": typerecursion, "argsval": argsval, "kwargsval": kwargsval, "nonkeyargs": nonkeyargs, "multiplyargs": multiplyargs,
            "kwargsval2": kwargsval2, "formated_kwargs": formated_kwargs, "args_and_kwargs": args_and_kwargs, "firstclassfunc": f("Emma"), "fun1": fun1(msg, "Alex"), "funcres": funcres(),
            "d_add": d["add"](5, 3), "d_subtract": d["subtract"](5, 3)}