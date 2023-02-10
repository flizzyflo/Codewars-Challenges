

def valid_parenthesis(string: str) -> bool:

    bracket_tracking_stack: list[str] = []
    open_brackets: tuple[str] = tuple("([{")
    closed_brackets: tuple[str] = tuple(")]}")
    bracket_pairs: dict[str, str] = dict(zip(open_brackets, closed_brackets))

    for current_bracket in string:
        if current_bracket in open_brackets:
            # insert required closing bracket into stack
            bracket_tracking_stack.append(bracket_pairs[current_bracket])

        if current_bracket in closed_brackets:
            # check if current bracket is closing bracket, and if, grab the required closing bracket

            if not bracket_tracking_stack or current_bracket != bracket_tracking_stack.pop():
                # compare, if true all good
                return False

    return len(bracket_tracking_stack) == 0

