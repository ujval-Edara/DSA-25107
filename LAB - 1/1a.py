def countdown(n):
    # av.sc.u4cse25107
    if n <= 0:
        print("Launch!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)