# Class
# A class is a blueprint or template used to create objects. It defines the structure that specifies the data members (attributes) and functions (methods) an object will contain. A class typically contains two main components:

# 1. Attributes (Data Members): Attributes are the properties or characteristics of an object. They store information related to the object.

# 2. Methods (Functions): Methods define the actions or behaviors that an object can perform.

# Features of a Class

# Describes the data and operations related to a particular entity.
# Serves as a reusable template from which multiple objects can be created.
# Helps organize code by grouping related variables and functions.
# Supports modular programming, making programs easier to understand and maintain.

# class in python
class car:
    def __init__(self,car,brand):
        self.car = car
        self.brand = brand
    def display(self):
        return f"car: {self.car}, brand: {self.brand}"
    
# Example usage
my_car = car("Model S", "Tesla")
print(my_car.display())  # Output: car: Model S, brand: Tesla


# Object
# An object is an instance of a class. It represents a real-world entity created using the class blueprint

# Stores actual values for class attributes.
# Allows you to call methods defined in the class.
# Multiple objects can exist from the same class, each holding different data.

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"name: {self.name}, age: {self.age}"
print(person("Alice", 30).display())  # Output: name: Alice, age: 30
# 
class A(object):
    def __new__(cls):
        print("Creating instance")
        return None
class B(object):
    def __init__(self):
        print("Initializing instance")
        return None

print(A())
print(B())


# Stack using class and objects

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,i):
        self.stack.append(i)
    def pop(self):
        self.stack.pop()
    def display(self):
        return self.stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.display())  # Output: [1, 2, 3]
s.pop()
print(s.display())  # Output: [1, 2]
