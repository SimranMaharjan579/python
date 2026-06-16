# Simple Calculator

# Taking input from user

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number: "))

# Choosing operator
operation = input("Enter operation (+, -, *, /): ")

#Performing calculation
if operation == "+":
    result = num1 +num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 *num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    result = "Invalid operation" 

# Output
print("Result: ", result)            
