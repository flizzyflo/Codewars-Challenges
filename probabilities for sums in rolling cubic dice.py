

def rolldice_sum_prob(sum_: int, dice_amount: int) -> float:
    import itertools
    sum_count, results = list(), list() 
    face_value = 6                                                                                 
    
    sum_count = list(itertools.product(range(1, face_value + 1), repeat=dice_amount))  #itertools.product creates pairs of face values

    for pairs in sum_count:
        if sum(pairs) == sum_:
            results.append(pairs)
     
    print(results)
    return len(results) / (face_value ** dice_amount)             
    
print(rolldice_sum_prob(8, 2))
