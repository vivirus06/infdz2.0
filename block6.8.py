class Animal:
    def reply(self):
        self.speak()

class Mammal(Animal):
    pass

class Cat(Mammal):
    def speak(self):
        print("meow")

class Primate(Mammal):
    def speak(self):
        print("Hello world!")

class Hacker(Primate):
    pass  # Removes speak method to default to a superclass

# Тестирование
if __name__ == '__main__':
    spot = Cat()
    spot.reply()  # Выводит "meow"

    data = Hacker()
    data.reply()  # Выводит "Hello world!"
