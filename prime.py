for n in range(2, 101):
    pri = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            pri = False
            break
    if pri:
        print(n, end=' ')
