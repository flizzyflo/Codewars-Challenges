

def sum_pairs(input_list: list[int], desired_sum: int) -> list[int, int]:
    
    cache = set()
    for i in input_list:
        
        # desired sum - i in cache, then the result has to be 'desired sum - i' and 'i'
        # example: desired sum 10, i =6, 4 is in cache. 10-6 in cache => 4, 6 are the solution
        if (desired_sum - i) in cache:
            
            return [desired_sum - i, i]
        
        cache.add(i)

    return [None]
