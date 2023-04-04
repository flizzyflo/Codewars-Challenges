def order_food(lst):
    meal_count: dict[str, int] = {}
    for item in lst:
        if item['meal'] not in meal_count:
            meal_count[item['meal']] = 1
        else:
            meal_count[item['meal']] += 1
        
    return meal_count
