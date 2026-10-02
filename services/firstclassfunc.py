def msg(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
f = msg

# Calling the function using the variable
#print(f("Emma"))



def msg(name):
    return f"Hello, {name}!"

def fun1(fun2, name):
    return fun2(name)

# Passing the msg function as an argument
#print(fun1(msg, "Alex"))

#Returning Functions from Other Functions


def fun11(msg):
    def fun22():
        return f"Message: {msg}"
    return fun22

# Getting the inner function
funcres = fun11("Hello, World!")
#print(funcres())


#Storing Functions in Data Structures
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
#print(d["add"](5, 3))       
#print(d["subtract"](5, 3))
