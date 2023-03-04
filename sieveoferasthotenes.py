

def get_all_primes_up_to(*, number: int) -> list[bool]:

    """
    Function to calculate and check whether numbers up to a specific boundary are primes or not. Takes the upper
    boundary as argument and returns a list with tuples of booleans either true or false, depending on being a prime or
    not and the corresponding index position representing the value of the number checked.

    @param number: upper limit bound until where the evaluation of prime numbers should be done.
    @return: tuple of numbers and booleans. Each true value is the prime number,
    the index position is the corresponding number. Both are returned as a tuple. E.g. (7, True) means 7 is a prime.
    """

    # initiate primes list with all numbers primes with size of desired amount
    is_prime = [True] * (number + 1)

    # iterate over the range of numbers. sqrt is enough, since multiples can not be primes per definition.
    for i in range(2, int(number ** 0.5) + 1):

        # if i is non-prime ( == false) ignore and loop over i
        if is_prime[i]:
            # if i is prime, then multiples of i can not be primes. thus, they can be set to false
            # if i is prime, the first non-prime has to be the first multiple of i and not i itself.
            first_non_prime = i + i

            # iterate over all multiples of i and set them to false
            for prime_index in range(first_non_prime, number, i):
                is_prime[prime_index] = False

    return [(number_value, prime) for number_value, prime in enumerate(is_prime)]


if __name__ == '__main__':

    upper_limit = input("Until which number the primes should be checked? Enter a positive number: ")

    if not upper_limit.isnumeric():
        raise ValueError(f"Please enter a number greater than '2'.'{upper_limit}' is not a number.")

    upper_limit = int(upper_limit)

    if upper_limit <= 2:
        raise ValueError(f"Please enter a valid number greater than '2'.'{upper_limit}' is not a valid number.")

    else:
        primes_list = get_all_primes_up_to(number=upper_limit)
        print(primes_list)
