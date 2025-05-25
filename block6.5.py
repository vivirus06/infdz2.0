set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Intersection:", set1 & set2)  # Intersection: {3, 4}
print("Union:", set1 | set2)         # Union: {1, 2, 3, 4, 5, 6}

# б) Создайте множество из строки и поэкспериментируйте с его индексированием.
string_set = set("abcde")
try:
    print(string_set[0])  # TypeError: 'set' object does not support indexing
except TypeError as e:
    print(e)

# в) Попробуйте пройти по элементам внутри строкового множества, используя цикл for. Какие методы запускаются на этот раз?
string_set = set("abcde")
for item in string_set:
    print(item) # Итерируется в произвольном порядке.

# г) Попробуйте получить пересечение и объединение строкового множества и простой строки Python. Работает ли это?
string_set = set("abcde")
string = "cdefg"

try:
    print(string_set & string) # TypeError: unsupported operand type(s) for &: 'set' and 'str'
except TypeError as e:
    print(e) # Нужно преобразовывать строку в множество:
print(string_set & set(string)) # {'e', 'd', 'c'}
print(string_set | set(string)) # {'e', 'd', 'c', 'b', 'a', 'g', 'f'}

# д) Расширьте свое множество, создав подкласс для обработки произвольно большого количества операндов с применением формы аргументов *args.
class MultiSet(set):
    def intersection(self, *others):
        result = self.copy()  # Стартуем с копии текущего множества
        for other in others:
            result &= other  # Пересечение с каждым множеством
        return result

    def union(self, *others):
        result = self.copy()
        for other in others:
            result |= other
        return result

# Вычислите пересечения и объединения множества операндов с помощью нового подкласса множества.
mset1 = MultiSet({1, 2, 3, 4})
mset2 = MultiSet({3, 4, 5, 6})
mset3 = MultiSet({4, 5, 6, 7})

print("Multi-Intersection:", mset1.intersection(mset2, mset3)) # Multi-Intersection: {4}
print("Multi-Union:", mset1.union(mset2, mset3))         # Multi-Union: {1, 2, 3, 4, 5, 6, 7}

# Как можно получить пересечение трех и более множеств, учитывая наличие у операции & только двух сторон?
# Применяйте reduce:
import functools
sets = [set1, set2, set3]
print(functools.reduce(lambda a, b: a & b, sets))
