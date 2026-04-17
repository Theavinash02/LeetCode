# Basic for loop
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # for new line

# for each loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

# for loop with multiple variables
for i, fruit in enumerate(fruits):
    print(f"Index: {i}, Fruit: {fruit}")

# for loop with else
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed")  # Output: Loop completed

#Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# for loop with striped input
for i in range(1,10,2):
    print(i, end=" ")  # Output: 1 3 5 7 9


    

