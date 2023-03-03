def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]


print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))