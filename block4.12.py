import timeit
import math
from functools import reduce
import operator

number = 10
N = 6  # Пример числа для вычисления факториала

def fact_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fact_recursive(n - 1)

def fact_reduce(n):
    return reduce(operator.mul, range(1, n + 1), 1)

def fact_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_math(n):
    return math.factorial(n)


def timer(func, reps, number):
    t = timeit.Timer(func)
    return min(t.repeat(repeat=3, number=number))

t1 = timer(lambda: fact_recursive(N), reps = 1000, number = 1000)
t2 = timer(lambda: fact_reduce(N), reps = 1000, number = 1000)
t3 = timer(lambda: fact_loop(N), reps = 1000, number = 1000)
t4 = timer(lambda: fact_math(N), reps = 1000, number = 1000)

print("Recursive:", t1)
print("Reduce:", t2)
print("Loop:", t3)
print("Math.factorial:", t4)
