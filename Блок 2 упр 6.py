D = {'a': 1, 'b': 2, 'c': 3}
try:
    print(D['d'])
except KeyError:
    print("Ошибка: Ключа 'd' нет в словаре!")
D['d'] = 'spam'
print(D)
