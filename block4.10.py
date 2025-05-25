import timeit
import math

reps = 100000
number = 10

def timer(func, reps, number):
    t = timeit.Timer(func)
    return t.repeat(repeat=3, number=number)


def f1():
    x = 144
    math.sqrt(x)

def f2():
    x = 144
    x ** .5

def f3():
    x = 144
    pow(x, .5)


t1 = min(timer(f1, reps, number))
t2 = min(timer(f2, reps, number))
t3 = min(timer(f3, reps, number))


print("math.sqrt(x):", t1)
print("x ** .5:", t2)
print("pow(x, .5):", t3)
print("math.sqrt is faster with the ratio:", t2/t1)
print("x**.5 is faster with the ratio:", t1/t2)
# Как бы вы измеряли скорость выполнения включений словарей по сравнению с циклами for в интерактивной подсказке?
# Пример:
# timeit.timeit("{x: x**2 for x in range(10)}", number=1000)
# timeit.timeit("d = {}; for x in range(10): d[x] = x**2", number=1000)
