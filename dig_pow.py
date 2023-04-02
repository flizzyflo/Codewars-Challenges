def dig_pow(number: int, power: int) -> int:

    power_sum: int = 0
    multiplier: int = 0
    for power, n in enumerate(str(number), power):
        # power_sum which should be calculated.
        power_sum += pow(int(n), power)

    while True:

        if number * multiplier == power_sum:
            return multiplier

        elif number * multiplier > power_sum + 1:
            return -1

        else:
            multiplier += 1


print(dig_pow(41, 5))
