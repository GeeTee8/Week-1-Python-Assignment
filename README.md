# Simple Calculator

A basic command-line calculator that performs arithmetic operations on two numbers.

## Description

This Python script implements a simple calculator that prompts the user for two numbers and a mathematical operation, then displays the result. It supports the four basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Division by zero error handling
- Input validation for operations
- Clean formatted output

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```bash
   python calculator.py
   ```

2. Follow the prompts:
   - Enter the first number
   - Enter the second number
   - Choose an operation (+, -, *, /)

3. The result will be displayed in the format: `number1 operation number2 = result`

## Example

```
Input first number: 10
Input second number: 5
Enter an operation (+, -, *, /): +
10 + 5 = 15
```

## Error Handling

- **Division by Zero**: If you attempt to divide by zero, the program will display "Error: Operation is Underfined"
- **Invalid Operation**: If you enter an operation other than +, -, *, or /, the program will display "Invalid operation. Please choose +, -, *, or /."
- **Invalid Number Input**: If non-numeric input is provided for the numbers, Python will raise a ValueError

## Code Structure

The calculator uses a simple if-elif-else structure to:
1. Get user input for two numbers and an operation
2. Check which operation was selected
3. Perform the calculation
4. Display the result with appropriate formatting
5. Handle edge cases (division by zero, invalid operations)

## Potential Improvements

- Add support for more operations (exponentiation, modulo, etc.)
- Implement a loop to perform multiple calculations
- Add more robust input validation
- Fix the typo in "Underfined" (should be "Undefined")
- Handle floating-point precision issues
- Add a graphical user interface