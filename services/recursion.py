#This code defines a recursive function to calculate factorial of a number, where function repeatedly 
# calls itself with smaller values until it reaches the base case.

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

resfact = []

resfact.append(factorial(5))


#This code defines a recursive function to calculate nth Fibonacci number, where each number is the sum of the two preceding ones, starting from 0 and 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

resfib = []
resfib.append(fibonacci(10))
#print(fibonacci(10))

#Types of Recursion


"""
Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. Some languages can optimize this to work like a loop, saving memory.
Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.
"""

def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    if n == 0:
        return 1
    else:
        return n * nontail_fact(n-1)

typerecursion = []
typerecursion.append(tail_fact(5))
typerecursion.append(nontail_fact(5))

#print(tail_fact(5))  
#print(nontail_fact(5))