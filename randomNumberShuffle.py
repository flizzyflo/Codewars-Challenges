
import random

def generate_random_numbers(amount_of_numbers: int, min_value: int, max_value: int) -> int:

    i: int = 0

    while i <= amount_of_numbers:
        yield random.randint(min_value, max_value)
        i += 1
c = 0
while c < 6:
    print(list(generate_random_numbers(6, 1, 50)))

    c += 1