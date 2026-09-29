from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/tuto",
    tags=["Tutoitems"]
)


@router.get("/datatypes")
async def data_types():

    x = 5
    name  = "Riky"

    a = 5
    b = 5.0
    c = 2 + 4j

    print(type(a))
    print(type(b))
    print(type(c))

    s = 'Welcome to the riky world'
    print(s)
    print(type(s))

    print(s[1])
    print(s[-1])
    
    real, imag = c.real, c.imag
    alist = [1, 2, 3]

    blist = ["Riky", "Mac", "Olv", 4, 5]
    b3 = blist[3]
    bm3 = blist[-3]


    return  { "x" : x, "name" : name, "a" : a, "b" : b, "real": real , "imag" : imag ,
              "alist" : alist , "blist" : blist , "b3" : b3, "bm3" : bm3 , "s":s}