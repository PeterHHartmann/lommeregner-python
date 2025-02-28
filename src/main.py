from enum import Enum
import math


def input_with_exit(prompt=""):
    raw_input = input(prompt)
    if raw_input.strip() == "Q":
        print("Exiting calculator.")
        exit()
    return raw_input


def get_number() -> float:
    number = None
    while number == None:
        try:
            raw_input = input_with_exit("Enter a number: ")
            number = float(raw_input)
        except ValueError:
            print("ERROR - Input is not a number.")
    return number


class CalcOperator(str, Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    SQUARED = "sqrt"
    EXPONENT = "^"


def get_operator() -> CalcOperator:
    possible_operators = [e.value for e in CalcOperator]
    operator_input = None
    while operator_input not in possible_operators:
        raw_input = input_with_exit("Enter an operator (+, -, *, /, sqrt, ^): ")
        operator_input = raw_input.strip()
        if operator_input not in possible_operators:
            print("ERROR - Please enter a valid operator.")
    return operator_input


def add(first_number, last_number) -> float:
    return first_number + last_number


def subtract(first_number, last_number) -> float:
    return first_number - last_number


def multiply(first_number, last_number) -> float:
    return first_number * last_number


def divide(first_number, last_number) -> float:
    result = None
    while result == None:
        try:
            result = first_number / last_number
        except ZeroDivisionError:
            print("ERROR - Cannot divide by zero.")
            last_number = get_number()
    return result


def square(last_number) -> float:
    return math.sqrt(last_number)


def exponent(first_number, last_number) -> float:
    return first_number**last_number


def get_calculation(first_number, operator, last_number) -> dict:
    msg = f"{first_number} {operator} {last_number} = "
    if operator == CalcOperator.SUBTRACT.value:
        result = subtract(first_number, last_number)
    elif operator == CalcOperator.MULTIPLY.value:
        result = multiply(first_number, last_number)
    elif operator == CalcOperator.DIVIDE.value:
        result = divide(first_number, last_number)
    elif operator == CalcOperator.SQUARED.value:
        result = square(last_number)
        msg = f"{operator}({last_number}) = "
    elif operator == CalcOperator.EXPONENT.value:
        result = exponent(first_number, last_number)
        msg = f"{first_number}^{last_number} = "
    else:
        result = add(first_number, last_number)
    return {
        "result": result,
        "msg": msg + str(result),
    }


def loop() -> None:
    should_stop = False
    while not should_stop:
        first_number = get_number()
        chosen_operator = get_operator()
        last_number = get_number()
        calculation = get_calculation(first_number, chosen_operator, last_number)
        print(calculation["msg"])
        print()


def main() -> None:
    print("-- Calculator --")
    print("To exit anytime enter 'Q'")
    loop()


if __name__ == "__main__":
    main()
