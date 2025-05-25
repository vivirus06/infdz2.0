class MyList: # Предыдущая версия
    def __init__(self, initial_value=None):
        if initial_value is None:
            self.data = []
        elif isinstance(initial_value, MyList):
            self.data = initial_value.data[:]  # Copy from another MyList
        else:
            self.data = list(initial_value)  # Copy from a list
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self.data + other.data)
        else:
            return MyList(self.data + list(other))

    def __radd__(self, other): # handles list + MyList
        return MyList(list(other) + self.data)

    def __mul__(self, other):
        return MyList(self.data * other)

    def __rmul__(self, other):
        return MyList(self.data * other)

    def __repr__(self): # string representation for printing
        return "MyList: " + str(self.data)

    def append(self, item):
        self.data.append(item)

    def sort(self, *args, **kwargs):
        self.data.sort(*args, **kwargs)

class MyListSub(MyList):
    add_count = 0  # Классовый атрибут, разделяется между всеми экземплярами

    def __add__(self, other):
        print("Calling + operator")
        MyListSub.add_count += 1
        return super().__add__(other) # super() для вызова __add__ из родительского класса

    def print_add_count(self):
        print("Add count:", MyListSub.add_count) # Обращение к классовому атрибуту

# Интерактивное тестирование
a = MyListSub([1, 2, 3])
b = MyListSub([4, 5, 6])
c = a + b  # Calling + operator
c.print_add_count()
d = a + [7, 8, 9] # Calling + operator
a.print_add_count()
print(a.add_count)
