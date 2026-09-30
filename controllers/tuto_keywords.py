from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import keyword

router = APIRouter(
    prefix="/tuto",
    tags=["Tutokwords"]
)

@router.get("/keywords")
async def keywords():
    #print("The list of keywords are : ")
    #print(keyword.kwlist)

    return {"keywords": keyword.kwlist}