def addDict(dict1, dict2):
    new_dict = dict1.copy()  # Создаем копию dict1, чтобы не изменять его
    for key in dict2:
        new_dict[key] = dict2[key] # Перезаписываем существующие ключи, если нужно.
    return new_dict

# Альтернативный вариант (используя update):
# def addDict(dict1, dict2):
#    new_dict = dict1.copy()
#    new_dict.update(dict2)
#    return new_dict

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
dict_c = addDict(dict_a, dict_b)

print(dict_a)
print(dict_b)
print(dict_c)  # {'a': 1, 'b': 3, 'c': 4}


# Что произойдет, если передать списки вместо словарей?
# print(addDict([1,2], [3,4])) # TypeError: 'list' object has no attribute 'copy'

# Как можно было бы обобщить функцию для обработки такого случая?
def add_dicts_generalized(arg1, arg2):
    if type(arg1) is dict and type(arg2) is dict:
        return addDict(arg1, arg2)
    else:
        print("Error: Both arguments must be dictionaries.")
        return None  # Или выдать исключение

print(add_dicts_generalized(dict_a, dict_b))
print(add_dicts_generalized([1,2], [3,4]))

# Имеет ли значение порядок, в котором передаются аргументы?
dict_d = addDict(dict_b, dict_a)
print(dict_d) # {'b': 2, 'c': 4, 'a': 1} - теперь "b" имеет значение из dict_a
