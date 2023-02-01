
def isPrime(number: int) -> bool:

    if not isinstance(number, int):
        return False

    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True
