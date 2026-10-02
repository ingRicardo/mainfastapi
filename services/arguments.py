
# *args example
def fun(*args):
    return sum(args)

argsval = []
argsval.append(fun(5, 10, 15))
#print(argsval)

kwargsval = []

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        kwargsval.append((k, val))


fun(a=1, b=2, c=3)
#print(kwargsval)

#Symbols for Handling Variable Arguments
# Non-Keyword Arguments (*args)

nonkeyargs = []
def myFun(*argv):
    for arg in argv:
        nonkeyargs.append(arg)

myFun('Hello', 'Welcome', 'to', 'RikyMac', 'Python', 'Tutorial')

multiplyargs = []
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

multiplyargs.append(multiply(2, 3, 4))

# Keyword Arguments (**kwargs)

kwargsval2 = []
def fun(**kwargs):
    for k, val in kwargs.items():
        kwargsval2.append((k, val))

fun(s1='Python', s2='is', s3='Awesome')

formated_kwargs = []
def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

formated_kwargs.append(introduce(Name="Alice", Age=25, City="New York"))

#Using both *args and **kwargs
args_and_kwargs = []
def student_info(*args, **kwargs):
    args_and_kwargs.append((args, kwargs))
    #print("Subjects:", args)        # Positional arguments
    #print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")