
def tribonacci(signature: list[int], n: int) -> list[int]:

    """Takes a list on integer as input. Adds integer to the signature
    until the legth is n. Returns the list. Numbers to be added are calculated
    as sum of the former 3 digits."""

    count = 3
    if n == 0:

        return []

    else:
        while count < n:
            signature.append(signature[-3] + signature[-2] + signature[-1])
            count += 1

        return signature[:n]
