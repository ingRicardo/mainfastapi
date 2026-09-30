
def greet():
    msg = "Hello from inside the function!"
    return msg

msg = "Python is awesome!"

def display():
    return "Inside function:", msg

display()

displayvar = ("Outside function:", msg)


#Use of Local and Global variables

def funlocal():
    ss = "Me too."
    return ss

ss = "I love RikyMacias"

#Use of Local and Global variables
sg = "Python is great!"
globalvar =[]
def funglobal():
    global sg
    sg += " GFG"   # Modify global variable
    globalvar.append(sg)
    sg = "Look for Riky Python Section"  # Reassign global
    globalvar.append(sg)


funglobal()
globalvar.append(sg)

#Global vs Local with Same Name

glovslocal = []
a = 1  # Global variable

def f():
   glovslocal.append("f():")  # Uses global a
   glovslocal.append(a)
def g():
    a = 2  # Local shadows global
    glovslocal.append("g():")
    glovslocal.append(a)

def h():
    global a
    a = 3  # Modifies global a
    glovslocal.append("h():")
    glovslocal.append(a)

glovslocal.append("global:")
glovslocal.append(a)

f()
glovslocal.append("global:")
glovslocal.append(a)

g()
glovslocal.append("global:")
glovslocal.append(a)

h()
glovslocal.append("global:")
glovslocal.append(a)



