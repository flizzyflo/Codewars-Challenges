
def productFib(target_product: int, counter: int = 1) -> list[int, int, bool]:
    
    """Creates a fibonacci sequence and returns the closest fibonacci numbers or the
    two fibonacci numbers to get to number prod, as well as a boolean if fibonacci numbers
    multiplied are prod or not."""
    
    fib_sequence = [0, 1]

    while fib_sequence[counter - 1] * fib_sequence[counter] < target_product:
        fib_sequence.append(fib_sequence[counter - 1] + fib_sequence[counter])
        counter += 1

    return [fib_sequence[-2], fib_sequence[-1], fib_sequence[-2] * fib_sequence[-1] == target_product]

print(productFib(5895))

