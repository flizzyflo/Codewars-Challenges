import re


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile(r"\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {"+": self.addition,
                          "-": self.subtraction,
                          "*": self.multiplication,
                          "/": self.division,
                          "%": self.modulo,
                          "=": self.equality}

        self.special_operators = ["*", "/", "%"]
        self.parentheses_pairs: dict[str, str] = {"(": ")", "[": "]"}


    def multiplication(self, left, right):
        if left in self.vars.keys() and right in self.vars.keys():
            return self.vars[left] * self.vars[right]
        elif left in self.vars.keys():
            return self.vars[left] * right
        elif right in self.vars.keys():
            return left * self.vars[right]
        else:
            return left * right

    def division(self, left, right):
        if left in self.vars.keys() and right in self.vars.keys():
            return self.vars[left] / self.vars[right]
        elif left in self.vars.keys():
            return self.vars[left] / right
        elif right in self.vars.keys():
            return left / self.vars[right]
        else:
            return left / right

    def modulo(self, left, right):
        if left in self.vars.keys() and right in self.vars.keys():
            return self.vars[left] % self.vars[right]
        elif left in self.vars.keys():
            return self.vars[left] % right
        elif right in self.vars.keys():
            return left % self.vars[right]
        else:
            return left % right

    def addition(self, left, right):
        if left in self.vars.keys() and right in self.vars.keys():
            return self.vars[left] + self.vars[right]
        elif left in self.vars.keys():
            return self.vars[left] + right
        elif right in self.vars.keys():
            return left + self.vars[right]
        else:
            return left + right

    def subtraction(self, left, right):
        if left in self.vars.keys() and right in self.vars.keys():
            return self.vars[left] - self.vars[right]
        elif left in self.vars.keys():
            return self.vars[left] - right
        elif right in self.vars.keys():
            return left - self.vars[right]
        else:
            return left - right

    def equality(self, left, right):
        self.vars[left] = right
        return self.vars[left]

    def get_value_of(self, variable):
        return self.vars[variable]

    def contains_parentheses(self, expression: list[str]) -> bool:
        return any([True if item in self.parentheses_pairs.keys() else False for item in expression])

    def has_valid_parentheses(self, expression: list[str]) -> bool:
        open_parenthesis: str = list()

        for parenthesis in expression:
            if parenthesis in self.parentheses_pairs.keys():
                open_parenthesis.append(parenthesis)

            if parenthesis in self.parentheses_pairs.values():
                try:
                    open_parenthesis.pop()

                except IndexError as ie:
                    # print(ie, "list is empty")
                    return False

        return len(open_parenthesis) == 0

    def collect_sub_expressions(self, expression: list[str]) -> list[int, int]:

        open_par: list[int] = list()
        sub_expressions: list[tuple[int, int]] = list()
        visited_indices: set[int] = set()
        idx: int = 0

        while True:

            if idx >= len(expression):
                return sub_expressions

            if idx in visited_indices:
                continue

            if expression[idx] in self.parentheses_pairs.keys():
                open_par.append(idx)
                visited_indices.add(idx)

            if expression[idx] in [")", "]"]:
                visited_indices.add(idx)

                sub_expressions.append((open_par.pop(), idx))

            idx += 1


    def input(self, expression):

        # generate tokens out of expression
        # returns a splitted list of all single elements of the expression

        if not expression or expression == " ":
            return ""

        tokens = tokenize(expression)

        # asking for variable value
        if len(tokens) == 1 and self.is_letter(tokens[0]):

            if self.is_stored_as_variable(tokens[0]):
                return self.vars[tokens[0]]

            else:
                raise Exception("Invalid identifier. No variable with name 'y' was found.")

        # base case direct variable assignement
        if len(tokens) == 3 and "=" in tokens:
            self.vars[tokens[0]] = tokens[2]
            return tokens[2]

        # distinguish parentheses or no parentheses case
        # case assignment of a complex calculation to a variable
        elif len(tokens) > 3 and tokens[1] == "=":
            new_variable = tokens[0]
            tokens = self.insert_variable_values(expression=tokens[2:])
            return self.equality(new_variable, self.evaluate_expression(expression=tokens))

        # case not an assignment but a calculation
        else:
            tokens = self.insert_variable_values(tokens)
            return self.evaluate_expression(expression=tokens)


    def is_stored_as_variable(self, token: str) -> bool:
        return token in self.vars.keys()

    def is_letter(self, token: str) -> bool:
        return token.isnumeric()

    def insert_variable_values(self, expression: list[str]) -> list[str]:

        # replaces variables within an expression with values of corresponding variable
        return [self.vars[variable] if variable in self.vars.keys() else variable for variable in expression]

    def evaluate_expression(self, expression: list[str]) -> int | float:

        result = float(expression[0])
        operator: str = None
        idx: int
        value: str

        # set to keep track of already calculated indices, in case an prioritized operation occurs
        visited_indices = {0}

        for idx, value in enumerate(expression):

            # Case the current index was already calculated.
            # Index will be skipped to avoid multiple caluclation of single index
            if idx in visited_indices:
                continue

            if value in self.functions.keys():

                if idx + 2 < len(expression) and expression[idx + 2] in self.special_operators and value not in self.special_operators:
                    # keep track of the former operator.
                    # use former operator to calculate complex expression, e.g. 3 + 5 * 2
                    # operator would be '*' and former operator '+'

                    former_operator: str = value
                    operator = expression[idx + 2]
                    visited_indices.add(idx + 1)
                    visited_indices.add(idx + 2)
                    visited_indices.add(idx + 3)

                    result = self.functions[former_operator](result,
                                                             self.functions[operator](float(expression[idx + 1]),
                                                                                      float(expression[idx + 3])))

                else:
                    # if the next operator is not a special operator, use current operator as operator
                    # example: 3 + 3 - 2 ; '+' would be the operator
                    operator = value

            else:
                # current value is not an operator, but a number instead
                result = self.functions[operator](float(result), float(value))

        return result


# To Do: Implement the parenthesis sub_expression into the calculation
# Fix bug with expressions like 2 * 2 * 5 * 4
#
#


if __name__ == '__main__':
    c = Interpreter()
    c.input("a = 3")
    c.input("b = 2")
    print(c.vars)
    x = "2 + (2 * 4 * 4) + 5 + 2 - 5"
    print(c.contains_parentheses(x))
   # print(c.input(x))
    st = c.collect_sub_expressions(x)
    for item in st:
        st, end = item
        e = tokenize(x[st + 1:end])
        e = c.insert_variable_values(e)
        ress = c.evaluate_expression(e)
        ttt = x.replace(x[st: end], str(ress))


