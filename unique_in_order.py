def unique_in_order(iterable: list[int] | str) -> list[int|str]:
    
    """
    Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

    For example:

    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3])       == [1,2,3]
    """
    
    
    if len(iterable) == 1:
        return [iterable[0]]
    
    curr_pos: int = 0
    iter_length: int = len(iterable) - 1
    result: list[int|str] = list()

    while curr_pos <= iter_length:
        
        if iterable[curr_pos] == iterable[curr_pos - 1]:
            curr_pos += 1
            continue
        
        result.append(iterable[curr_pos])
        curr_pos += 1
    
    if len(result) == 0 and len(iterable) > 0:
        return [iterable[0]]
    
    return result