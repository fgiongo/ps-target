def isFib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if a == n or b == n:
        return True
    else:
        return False

if isFib(int(input("> "))):
    print("O número pertence à sequência de Fibonacci")
else:
    print("O número não pertence à sequência de Fibonacci")
