class Attrs:
    def __setattr__(self, name, value):
        print(f"Setting attribute: {name} = {value}")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        print(f"Getting attribute: {name}")
        return super().__getattribute__(name)

# Интерактивное тестирование
a = Attrs()
a.x = 5  # Setting attribute: x = 5
print(a.x) # Getting attribute: x
           # 5
try:
    a + 1  # Getting attribute: __add__
except TypeError as e:
    print(e)
