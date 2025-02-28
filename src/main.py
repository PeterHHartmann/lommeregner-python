from enum import Enum


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


def get_operator() -> CalcOperator:
    possible_operators = [e.value for e in CalcOperator]
    operator_input = None
    while operator_input not in possible_operators:
        raw_input = input_with_exit("Enter an operator (+, -, *, /): ")
        operator_input = raw_input.strip()
        if operator_input not in possible_operators:
            print("ERROR - Please enter a valid operator.")
    return operator_input


def get_calculation(first_number, operator, last_number) -> float:
    calculation = None
    if operator == CalcOperator.ADD.value:
        calculation = first_number + last_number
    elif operator == CalcOperator.SUBTRACT.value:
        calculation = first_number - last_number
    elif operator == CalcOperator.MULTIPLY.value:
        calculation = first_number * last_number
    elif operator == CalcOperator.DIVIDE.value:
        while calculation == None:
            try:
                calculation = first_number / last_number
            except ZeroDivisionError:
                print("ERROR - Cannot divide by zero.")
                last_number = get_number()
    return f"{first_number} {operator} {last_number} = {calculation}"


def loop() -> None:
    should_stop = False
    while not should_stop:
        first_number = get_number()
        chosen_operator = get_operator()
        last_number = get_number()
        calculation = get_calculation(first_number, chosen_operator, last_number)
        print(calculation)
        print()


def main() -> None:
    print("-- Calculator --")
    print("To exit anytime enter 'Q'")
    loop()
    # first_number = get_number()
    # chosen_operator = get_operator()
    # last_number = get_number()
    # calculation = get_calculation(first_number, chosen_operator, last_number)
    # print(calculation)


if __name__ == "__main__":
    main()
