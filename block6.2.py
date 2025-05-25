class MyList:
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


# Интерактивное тестирование
l = MyList([1, 2, 3])
print(l)
l.append(4)
print(l)
print(l[0])
print(len(l))
print(l + [5,6])
print([5,6] + l)

# Дополнительные методы:
    def insert(self, index, object): self.data.insert(index, object)
    def pop(self, index=-1): return self.data.pop(index)
    def remove(self, value): self.data.remove(value)
    def extend(self, iterable): self.data.extend(iterable)
    def __iadd__(self, other):  # +=
        self.extend(other)
        return self

    def reverse(self): self.data.reverse()
    def index(self, value, start=0, stop=None):
        if stop is None:
            return self.data.index(value, start)
        else:
            return self.data.index(value, start, stop)
    def count(self, value): return self.data.count(value)
    def clear(self): self.data.clear() # Python 3.3+ only
    def copy(self): return MyList(self) # Returns a new MyList instance
