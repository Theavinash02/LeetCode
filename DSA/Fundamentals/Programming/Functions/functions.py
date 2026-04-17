#function in python
def greet(name):
    return "Hello, " + name + "!"
# Example usage
print(greet("Alice"))  # Output: Hello, Alice!

#function with default parameter
def greet(name="World"):
    return "Hello, " + name + "!"
# Example usage
print(greet())  # Output: Hello, World!

#function with variable number of positional arguments
def greet(*names):
    return "Hello, " + ", ".join(names) + "!"
# Example usage
print(greet("Alice", "Bob", "Charlie"))  # Output: Hello, Alice, Bob, Charlie!

#function with keyword arguments
def greet(greeting, name):
    return greeting + ", " + name + "!"
# Example usage
print(greet(greeting="Hi", name="Alice"))  # Output: Hi, Alice!

#function with return value
def add(a, b):
    return a + b
# Example usage
result = add(5, 3)
print(result)  # Output: 8

# function with variable number of keyword arguments
def add(**kwargs):
    return kwargs.get('a', 0) + kwargs.get('b', 0)
# Example usage
result = add(a=5, b=3)
print(result)  # Output: 8

# function with both Positional and Keyword Arguments
def demo(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    return sum(args) + sum(kwargs.values())
# Example usage
result = demo(5, 3,b = 4, d = 5, e= 8)  # c will take the default value of 0
print(result)  # Output: 25