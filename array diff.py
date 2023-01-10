
def array_diff(filtered_list: list, compared_list: list) -> list:

    """Returns the filtered list without the items of the compared list"""

    if not filtered_list or not compared_list:
        return []

    return [number for number in filtered_list if number not in compared_list]
        



            
