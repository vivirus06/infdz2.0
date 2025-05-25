def is_prime(y):
    if y <= 1:
        print(y, "is not prime")
        return

    x = int(y // 2)  # Приведение к int для правильной работы

    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            return
        x -= 1
    else:
        print(y, 'is prime')


is_prime(13)
is_prime(13.0)
is_prime(15)
is_prime(15.0)
is_prime(0)
is_prime(1)
is_prime(-5) # Обработка отрицательных чисел

import math

def is_prime_optimized(y):
    if y <= 1:
        print(y, "is not prime")
        return

    if y == 2: # Проверка особого случая
        print(y, "is prime")
        return

    if y % 2 == 0:  # Если четное
        print(y, "has factor 2")
        return

    x = int(math.sqrt(y)) + 1  # Проверка до квадратного корня
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            return
        x -= 1
    else:
        print(y, 'is prime')

print("Optimized version:")
is_prime_optimized(13)
is_prime_optimized(15)
