num_1 = int(input("Input first number: "))
num_2 = int(input("Input second number: "))
math_operation = input("Enter an operation (+, -, *, /): ")

if math_operation == "+":
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
elif math_operation == "-":
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result}")
elif math_operation == "*":
    result = num_1 * num_2
    print(f"{num_1} * {num_2} = {result}")
elif math_operation == "/":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}")
    else:
        print("Error: Operation is Underfined")
else:
    print("Invalid operation. Please choose +, -, *, or /.")