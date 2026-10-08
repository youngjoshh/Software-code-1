"""Simple calculator that takes user input."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend / divisor


def power(base, exponent):
    return base ** exponent


def modulo(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend % divisor


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulo,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /, ^, %): ").strip()
        if operation in OPERATIONS:
            return operation
        print("Unknown operation. Try again.")


def main():
    first = get_number("Enter first number: ")
    second = get_number("Enter second number: ")
    operation = get_operation()

    try:
        result = OPERATIONS[operation](first, second)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
