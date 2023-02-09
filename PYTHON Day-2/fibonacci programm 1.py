def fibonacci(n1):
    if n1 == 0:
        return 0
    elif n1 == 1:
        return 1
    else:
        return fibonacci(n1-1) + fibonacci(n1-2)

def waycount (n):
    return fibonacci(n+1)
n=2
print("The number of ways to reach the top of a staircase with", n, "steps is", waycount(n))
