from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import keyword


class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        pass  # Placeholder for greet method


router = APIRouter(
    prefix="/tuto",
    tags=["Tuto_3"]
)

def funZero():
    pass

def fun():
    return "Welcome to Riky"

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

def myFun(x, y=50):
    return  (x , y)

def student(fname, lname):
    return (fname, lname)

def nameAge(name, age):
    return [("Hi, I am", name), ("My age is ", age)]

def myFun2(*args, **kwargs):
    res =[]
    #print("Non-Keyword Arguments (*args):")
    res.append("Non-Keyword Arguments (*args):")

    for arg in args:
        #print(arg)
        res.append(arg)
    res.append("Keyword Arguments (**kwargs):")

    #print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        #print(f"{key} == {value}")
        res.append(f"{key} == {value}")

    return res

def f1():
    s = 'I love Riky Mac'
    def f2():
        return(s)

    return f2()

def sq_value(num):
    return num**2

def myFunmuta(x):
    x[0] = 20

def myFunimmuta(x):
    x = 20

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

    # functions
    res = fun()
    eveodd1 = evenOdd(16)
    eveodd2 = evenOdd(7)

    #Types of Function Arguments

    defparafunc = myFun(10)
    typeofdefpara = str(type(defparafunc))

    strres1 = student(fname='Geeks', lname='Practice')
    strres2 = student(lname='Practice', fname='Geeks')

    resnameage1 =  nameAge("Olivia", 27)

    resnameage2 = nameAge(27, "Olivia")

    resnametype = str(type(resnameage1))


    argsres= myFun2('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

    #Function within Functions
    innerfunc = f1()

    #Return Statement

    returnfunc = []
    returnfunc.append(sq_value(2))
    returnfunc.append(sq_value(-4))

    #Pass by Reference and Pass by Value
    mutares = ""
    immutares = ""
    b = [10, 11, 12, 13]
    myFunmuta(b)
    mutares = b

    a = 10
    myFunimmuta(a)
    immutares= a

    #Python pass Statement
    x = 10

    if x > 5:
        pass  # Placeholder for future logic
    else:
        print("x is 5 or less")

    passval = []
    for i in range(5):
        if i == 3:
            pass  # Do nothing when i is 3
        else:
            passval.append(i)

    p = Person("Emily", 30)
    type_p = str(type(p))

    funZero()

    return {"eligible" : eligible , "travel": travel, "person" :person, "discount": discount, "person2": s, "typeofnumber":numbertype,
            "loopvals": loopvals, "resfunction": res, "eveodd1" : eveodd1, "eveodd2": eveodd2, "defparafunc": defparafunc, "typeofdefpara": typeofdefpara,
            "strres1": strres1, "strres2":strres2, "resnameage1": resnameage1, "resnameage2": resnameage2, "resnametype": resnametype,
            "argsres": argsres, "innerfunc": innerfunc, "returnfunc": returnfunc, "mutares": mutares, "immutares": immutares, "passval": passval,
            "personclass": p , "type_p": type_p}
