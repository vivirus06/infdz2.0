import math

numbers = [2, 4, 9, 16, 25]

# 1. Цикл for:
squares_for = []
for num in numbers:
    squares_for.append(math.sqrt(num))
print("For loop:", squares_for)

# 2. Вызов map:
squares_map = list(map(math.sqrt, numbers))
print("Map:", squares_map)

# 3. Списковое включение (List comprehension):
squares_comprehension = [math.sqrt(num) for num in numbers]
print("List comprehension:", squares_comprehension)

# 4. Генераторное выражение:
squares_generator = (math.sqrt(num) for num in numbers)
print("Generator expression:", list(squares_generator))
