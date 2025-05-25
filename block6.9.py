class Actor:  # Optional: Base class for shared behavior
    def __init__(self, name):
        self.name = name
    def line(self):
        pass

class Customer(Actor):
    def __init__(self):
        super().__init__("Customer")

    def line(self):
        print(f"{self.name}: \"that's one ex-bird!\"")

class Clerk(Actor):
    def __init__(self):
        super().__init__("Clerk")

    def line(self):
        print(f"{self.name}: \"no it isn't...\"")

class Parrot(Actor):
    def __init__(self):
        super().__init__("Parrot")

    def line(self):
        print(f"{self.name}: None")  # Or just pass

class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()

# Тестирование
if __name__ == '__main__':
    import parrot
    parrot.Scene().action()
