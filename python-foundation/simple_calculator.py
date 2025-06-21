# Simple calculator using if-else

# Take inputs
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform operation based on input
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator entered.")
