
results_idx_numbers = []

def sum_pairs(int_list: list[int, int], desired_sum: int) -> list[int, int]:
    
    results_idx_numbers.clear()
 
    recursive_determination_of_idx(0, len(int_list) - 1, int_list, desired_sum)
    
    if len(results_idx_numbers) == 0:
        return None
    else:

        x,y = calcute_result(results_idx_numbers)
        return [int_list[x], int_list[y]]


def recursive_determination_of_idx(left_idx: int, right_idx: int, int_list: list[int, int], desired_sum: int):
    
    """Function calculates the index numbers which meet the required sum and adds them to the result list."""

    if left_idx >= right_idx:
        return None

    elif int_list[left_idx] + int_list[right_idx] == desired_sum and [left_idx, right_idx] not in results_idx_numbers:
        # basecase: sum is found, add indices to the result list

        results_idx_numbers.append([left_idx, right_idx])

        # 3 recursive cases: 
        # lefts_idx remains constant - right_idx decreases by 1
        # left_idx increases by 1 - right_idx remains constant
        # left_idx increases by 1 - right_idx decreases by 1
    else:
        recursive_determination_of_idx(left_idx, right_idx - 1, int_list, desired_sum) or recursive_determination_of_idx(left_idx + 1, right_idx, int_list, desired_sum) or recursive_determination_of_idx(left_idx + 1, right_idx - 1, int_list, desired_sum) 


def calcute_result(results: list[int, int]) -> list[int, int]:
    # differenz zwischen den indizes
    x = lambda x, y: y-x
    curr = []
    val: int = 1000000
    for i in results:
        t, u = i

        if x(t,u) < val:
            val = x(t, u)
            curr = [t, u]
    return curr
