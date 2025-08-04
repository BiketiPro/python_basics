# Basic calculator program

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Get user input for operator
operator = input("Enter operator (+, -, *, /): ")
# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation. Please choose from +, -, *, or /.")
