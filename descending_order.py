def descending_order(num):
    result_list = []
    for number in str(num):
        result_list.append(number)
    return int("".join(sorted(result_list, reverse=True)))
