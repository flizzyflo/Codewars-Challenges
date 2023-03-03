"""
    The purpose of this kata is to write a program that can do some algebra.

    Write a function expand that takes in an expression with a single, one character variable, and expands it.
    The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative,
    x is any single character variable, and n is a natural number.
    If a = 1, no coefficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.
    The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are
    the coefficients of the term, x is the original one character variable that was passed in the original
    expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing order.
    If the coefficient of a term is zero, the term should not be included.
    If the coefficient of a term is one, the coefficient should not be included.
    If the coefficient of a term is -1, only the "-" should be included.
    If the power of the term is 0, only the coefficient should be included.
    If the power of the term is 1, the caret and power should be excluded.

    Examples:
    test.assert_equals(expand("(x+1)^0"), "1")
    test.assert_equals(expand("(x+1)^1"), "x+1")
    test.assert_equals(expand("(x+1)^2"), "x^2+2x+1")

    test.assert_equals(expand("(x-1)^0"), "1")
    test.assert_equals(expand("(x-1)^1"), "x-1")
    test.assert_equals(expand("(x-1)^2"), "x^2-2x+1")

    test.assert_equals(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
    test.assert_equals(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
    test.assert_equals(expand("(7x-7)^0"), "1")
                                                                                  4 * a**4-1 * b      4 * b ** 4-1 * a
    test.assert_equals(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")  -> 4 * 5**3 * 3= 1500; 4 * 3 ** 3 * 5
    test.assert_equals(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
    test.assert_equals(expand("(-7x-7)^0"), "1")

    """
import math
import re


def expand(expression: str) -> str:
    
    """
    Expands a binomial expression passed in as string into its expanded form. Uses the binomial theorem
    to calculate the expanded expression.

    @param expression: binomial expression to be expanded. Should be in format '(a+bx)^n'
    @return: Expanded string format of the binomial expression. (a + b) ^ 2 => a^2 + 2ab + b^2
    """

    regex_pattern: str = '\\({1}(-?[0-9]{1,})*(-?[a-zA-Z]){1}\\+?(-?[0-9]*)\\){1}\\^{1}([0-9])'
    # splits expression into number, variable, multiplier
    # (-2x+3)^4 -> ["-2", "x", "+3", "4"]

    a, variable, b, exponent = re.split(pattern=regex_pattern,
                                        string=expression)[1:5]

    # type cast to integer for calculation later on
    exponent = int(exponent)
    b = int(b)

    if exponent == 0:
        return "1"

    if a is not None:
        # if a is within the formula, type cast to integer for calculation
        a = int(a)

    if variable[0] == "-":
        variable = variable[1:]
        a = -1

    solution: str = ""

    for k in range(0, exponent):
        iter_power_b = b ** k
        c = math.comb(exponent, k)
        total_val = c * iter_power_b

        exp_str = get_exponent(exponent, k)
        if (total_val == 1 and k > 0) or (total_val == 1 and a is None):
            # further iteration or first iteration with no a value
            total_val = ""
            solution += f"{total_val}{variable}{exp_str}"
            continue

        if a is not None:
            iter_power_a = a ** (exponent - k)
            total_val = c * iter_power_b * iter_power_a

        if total_val > 0 and solution != "":
            # add plus sign to value, if not empty string
            solution += "+"

        # case just a 1. 1 should not be displayed in front of the variable
        if total_val == 1:
            total_val = ""

        # case just a -1. -1 should not be displayed in front of the variable
        if total_val == -1:
            total_val = "-"

        solution += f"{total_val}{variable}{exp_str}"

    iter_power_b = b ** exponent

    if iter_power_b > 0:
        solution += "+"

    solution += str(iter_power_b)

    return solution


def get_exponent(exponent: int, k: int) -> str:

    """
    Helper function to calculate the exponent of the specific part of the expanded form of the binomial expression.
    @param exponent: exponent passed in as integer
    @param k: iteration counter passed in as integer
    @return: either exponent number as a string or empty string if exponent == 1
    """

    if (exponent - k) == 1:
        return ""

    else:
        return f"^{exponent - k}"


if __name__ == '__main__':
    bin_exp = "(-p-13)^2"
    print(expand(expression=bin_exp))
