
def incrementer(nums: list) -> list:
    result = list()
    for index, number in enumerate(nums):
        if index + number + 1> 9:
            temp = [index + number + 1]
            for item in temp:
                result.append(int(str(item)[len(str(item)) - 1:len(str(item))]))
        else:
            result.append(index + number + 1)

    return result
