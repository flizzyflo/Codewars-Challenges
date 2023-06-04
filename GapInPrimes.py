
def isPrimeNumber(number: int)-> bool:
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
        else:
            return True


def step(step: int, start_number: int, end_number: int) -> list:

    not_prime_number = []

    for number in range(start_number, end_number + 1):

        if number + step + 1 > end_number:
            return None

        if number in not_prime_number:
            continue

        if isPrimeNumber(number) and isPrimeNumber(number + step):
            return [number, number + step]


        elif not isPrimeNumber(number + step):
            not_prime_number.append(number + step)


    return None

print(step(16, 2000, 5100))