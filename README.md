# Example: Demonstrating all four OOPs concepts

class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def show_details(self):
        print(f"Vehicle: {self.name}, Mileage: {self.mileage}km/l")


# Inheritance
class Car(Vehicle):
    def __init__(self, name, mileage, seats):
        super().__init__(name, mileage)
        self.seats = seats

    # Polymorphism (method overriding)
    def show_details(self):
        print(f"Car: {self.name}, Mileage: {self.mileage}km/l, Seats: {self.seats}")


# Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
