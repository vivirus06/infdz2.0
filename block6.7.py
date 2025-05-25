class Food:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # String representation
        return f"Food('{self.name}')"

class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)

class Customer:
    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self):
        if self.food:
            print(f"Customer has ordered: {self.food.name}")
        else:
            print("Customer has not ordered anything.")


class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        self.customer.printFood()

# Тестирование
if __name__ == '__main__':
    meal = Lunch()
    meal.order("Pizza")
    meal.result() # Customer has ordered: Pizza
    meal.order("Burger")
    meal.result() # Customer has ordered: Burger
