

def sum_pairs(input_list: list, desired_sum: int):
    cache = set()
    
    for i in input_list:
        
        # desired sum - i in cache, then the result has to be 'desired sum - i' and 'i'
        if desired_sum - i in cache:
            
            return [desired_sum - i, i]
        
        cache.add(i)
    
