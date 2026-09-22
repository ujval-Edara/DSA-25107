def calculate_factorial(n):
    # av.sc.u4cse25107
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5))