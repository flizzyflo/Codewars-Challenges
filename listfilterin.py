def filter_list(array: list[str|int]) -> list[int]:
    
    """Filters all non-integer elements from the list passed in as argument"""

    def is_integer(element) -> bool:
        
        """Returns true if element is integer"""
        
        return isinstance(element, int)
    
    return list(filter(is_integer, array))
