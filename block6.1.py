class Adder:
    def add(self, x, y):
        print("Not Implemented")

    def __init__(self, data=None):
        self.data = data  # Data can be None, list or dict

    def __add__(self, other):  # Overload the + operator
        if self.data is None:
            raise TypeError("self.data must be initialized")
        return self.add(self.data, other)  # Pass data to add

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        new_dict = x.copy()
        new_dict.update(y)
        return new_dict

# Интерактивное тестирование
list_adder = ListAdder([1, 2, 3])
print(list_adder.add([4, 5, 6], [7, 8, 9]))  # [4, 5, 6, 7, 8, 9]
print(list_adder + [4, 5, 6])

dict_adder = DictAdder({'a': 1, 'b': 2})
print(dict_adder.add({'c': 3, 'd': 4}, {'e': 5, 'f': 6}))  # {'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(dict_adder + {'c': 3, 'd': 4}) # calls the add method and uses self.data
