def factorial(n, accumulator =1):
    if n ==0:
        return accumulator
    else :
        return factorial(n-1, accumulator*n)

print(factorial(6))