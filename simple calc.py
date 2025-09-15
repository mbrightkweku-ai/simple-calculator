# A simple calculator

num1 = int(input("enter the first number:  "))
operation = input("choose one operator : (*,+,/,-)  ")
num2 = int(input("enter the 2nd number:  "))

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2

else:
    result = "invalid operator"

print("Result : ", result)
