from app.operations import Operations

OPERATIONS = {
    "add": Operations.addition,
    "subtract": Operations.subtraction,
    "multiply": Operations.multiplication,
    "divide": Operations.division,
}


def calculator():
    """Run a REPL that performs addition, subtraction, multiplication, and division."""
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        func = OPERATIONS.get(operation)
        if func is None:
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue

        try:
            result = func(num1, num2)
        except ValueError as e:
            print(e)
            continue

        print(f"Result: {result}")