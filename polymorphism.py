"""
Polymorphism

Method overriding
implementing parent method in child method
same method name in different class- acts differently according to class
len(): different implementation for different data types
  - str 
  - dict
  - list

Method overloading
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


# class 