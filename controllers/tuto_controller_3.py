from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import keyword

router = APIRouter(
    prefix="/tuto",
    tags=["Tuto_3"]
)


@router.get("/tuto3")
async def tutorial_3():
    #Conditional Statements in Python

    eligible = ""
    age = 20
    if age >= 18:
        eligible = "Eligible to vote."

    #Short Hand if
    age = 19
    if age > 18: eligible = "Eligible to vote."

    travel =""

    age = 10
    if age <= 12:
        travel = "Travel for free." 
    else:
        travel= "Pay for ticket."

    age = 25
    person = ""
    if age <= 12:
        person ="Child."
    elif age <= 19:
        person ="Teenager."
    elif age <= 35:
        person ="Young adult."
    else:
        person ="Adult."

    age = 70
    is_member = True
    discount = ""

    if age >= 60:
        if is_member:
            discount="30% senior discount!"
        else:
            discount="20% senior discount."
    else:
        discount="Not eligible for a senior discount."

    #Conditional Expression (Ternary Operator)
    age = 20
    s = "Adult" if age >= 18 else "Minor"

    #Match-Case Statement
    number = 2
    numbertype=""
    match number:
        case 1:
            numbertype="One"
        case 2 | 3:
            numbertype="Two or Three"
        case _:
            numbertype="Other number"
    # loops

    loopvals=[]
    n = 4
    for i in range(0, n):
        loopvals.append(i)

    a = ["riky", "mac", "olv"]
    for idx in range(len(a)):
        loopvals.append(a[idx])

    cnt = 0
    while (cnt < 3):
        cnt = cnt + 1
        loopvals.append("Hello Rik")

    for i in range(1, 5):
        for j in range(i):
            loopvals.append(i)

    return {"eligible" : eligible , "travel": travel, "person" :person, "discount": discount, "person2": s, "typeofnumber":numbertype,
            "loopvals": loopvals}
