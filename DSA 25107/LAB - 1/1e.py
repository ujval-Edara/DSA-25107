def fibonacci(n):
    # av.sc.u4cse25107
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(terms):
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()

print_fibonacci_series(7)