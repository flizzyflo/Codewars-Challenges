
def get_order(order: str) -> str:

    """Filters the ordered items out of the order string and returns a result order string"""

    ordered_items: dict[str: int] = {"Burger":0, "Fries":0, "Chicken":0, "Pizza":0, "Sandwich":0, "Onionrings":0, "Milkshake":0, "Coke":0}
    start_index: int = 0

    for end_index, item in enumerate(order):
        
        if order[start_index : end_index + 1].capitalize() in ordered_items.keys():
            ordered_items[order[start_index : end_index + 1].capitalize()] += 1
            start_index = end_index + 1

        end_index += 1

    result_string =""
    counter = 0

    for key, value in ordered_items.items():
        while counter < value:
            result_string += key + " "
            counter += 1    

        counter = 0

    return result_string.rstrip()
    

print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))