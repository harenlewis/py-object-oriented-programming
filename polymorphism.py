"""
Polymorphism

Method overriding
implementing parent method in child method
same method name in different class- acts differently according to class
len(): different implementation for different data types
  - str 
  - dict
  - list

Method overloading (Not possible in python)
same method different parameters
def addition(a, b):
    c = a + b
    print(c)

def addition(a, b, c):
    d = a + b + c
    print(d)

Operator overloading
changing default of operator based on operands (values)
print method is the best example

print(2+5)
print("Hey" + "There")
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])


# Overloading + operator with magic method
class Book
    def __add__(self, other):
        return self.pages + other.pages

Similarliy
__mul__(self, other)
__lt__(self, other)
__le__(self, other)
__gt__(self, other) .....
"""


class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()

# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()

# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()
