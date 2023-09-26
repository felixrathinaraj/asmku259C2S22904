def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
n = 5  # You can change this number to calculate the factorial for a different value
result = factorial(n)
print(f"The factorial of {n} is {result}")