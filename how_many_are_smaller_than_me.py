
def smaller(array: list[int]) -> list[int]:

    # [3,2,2,1] -> [3, 1, 1, 0]
    # *Input[5, 4, 3, 2, 1] = > Output[4, 3, 2, 1, 0]
    # *Input[1, 2, 0] = > Output[1, 1, 0]

    number_idx: int = 0
    idx: int = number_idx + 1
    count: int = 0
    result_list: list[int] = list()

    while True:

        if idx >= len(array):
            result_list.append(count)
            number_idx += 1
            idx = number_idx + 1
            count = 0

        if idx >= len(array):
            result_list.append(count)
            return result_list

        if array[number_idx] > array[idx]:
            count += 1


        if number_idx >= len(array):
            return result_list

        idx += 1

if __name__ == "__main__":
    r = [1, 2, 0]
    print(smaller(r))