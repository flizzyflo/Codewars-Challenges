
def array_diff(list_to_filter: list[any], filter_list: list[any]) -> list[any]:

    """Returns the list_to_filter list without the items of the filter_list"""

    if not list_to_filter or not filter_list:
        return []

    return [list_element for list_element in list_to_filter if list_element not in filter_list]
        
r = ["a", "b"]
s = ["a", "c"]
print(array_diff(list_to_filter=r, filter_list=s))