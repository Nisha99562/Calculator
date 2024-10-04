def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        # Get user input
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()

        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue

        # Display the result
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
