def square_digits(num: int) -> int:
    result = str()
    for number in str(num):
        if number == 1:
            result += str(1 * 2)

        result += str(int(number) ** 2)
    return int(result)
