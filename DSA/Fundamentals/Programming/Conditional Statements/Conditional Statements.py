a  =5
# if statement
if a>0:
    print("a is positive")

# if-else statement
if a%2==0:
    print("a is even")
else:
    print("a is odd")

# if-elif-else statement
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")

#switch statement
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

#ternary operator
age = 20
status = "Adult" if age >=18 else "Not an adult"

#Nested ternary operator
score = 85
grade = "A" if score >=90 else "B" if score >=80 else "C" if score >=70 else "D" if score >=60 else "F"
print(grade)


