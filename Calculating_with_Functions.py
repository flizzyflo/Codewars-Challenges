"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
"""


def zero(math_operation: callable = None):
    if math_operation is None:
        return 0

    else:
        return eval(f"0 {math_operation}")


def one(math_operation: callable = None):
    if math_operation is None:
        return 1

    else:
        return eval(f"1 {math_operation}")


def two(math_operation: callable = None):
    if math_operation is None:
        return 2

    else:
        return eval(f"2 {math_operation}")


def three(math_operation: callable = None):
    if math_operation is None:
        return 3

    else:
        return eval(f"3 {math_operation}")


def four(math_operation: callable = None):
    if math_operation is None:
        return 4

    else:
        return eval(f"4 {math_operation}")


def five(math_operation: callable = None):
    if math_operation is None:
        return 5

    else:
        return eval(f"5 {math_operation}")


def six(math_operation: callable = None):
    if math_operation is None:
        return 6

    else:
        return eval(f"6 {math_operation}")


def seven(math_operation: callable = None):
    if math_operation is None:
        return 7

    else:
        return eval(f"7 {math_operation}")


def eight(math_operation: callable = None):
    if math_operation is None:
        return 8

    else:
        return eval(f"8 {math_operation}")


def nine(math_operation: callable = None):
    if math_operation is None:
        return 9

    else:
        return eval(f"9 {math_operation}")


def plus(number_function: callable):
    return f"+ {number_function}"


def minus(number_function: callable):
    return f"- {number_function}"


def times(number_function: callable):
    return f"* {number_function}"


def divided_by(number_function: callable):
    return f"// {number_function}"


if __name__ == '__main__':
    print(eight(minus(nine())))
