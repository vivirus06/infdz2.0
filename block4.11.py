def countdown(n):
    if n <= 0:
        print("stop")
    else:
        print(n, end=" ")
        countdown(n - 1)

countdown(5) # 5 4 3 2 1 stop

# Без рекурсии:
def countdown_iterative(n):
    while n > 0:
        print(n, end=" ")
        n -= 1
    print("stop")

countdown_iterative(5) # 5 4 3 2 1 stop

# С генератором:
def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1
    yield "stop"

for i in countdown_generator(5):
    print(i, end=" ")

#5 4 3 2 1 stop
