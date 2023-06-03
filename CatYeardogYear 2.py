def owned_cat_and_dog(cat_years, dog_years):
    owned_cat, owned_dog = 0, 0
    first_cat_year, first_dog_year = 15, 15
    second_cat_year, second_dog_year = 9, 9
    above_cat_years, above_dog_years = 4, 5


    if 15 <= cat_years < 24:
        owned_cat += 1
    else: 
        owned_cat = 0
    
    if 15 <= dog_years < 24:
        owned_dog += 1
    else:
        owned_dog = 0

    if cat_years == 24:
        owned_cat += 2

    if dog_years == 24:
        owned_dog += 2
    
    if cat_years > 24:
        owned_cat = int(((cat_years - first_cat_year - second_cat_year) / above_cat_years) + 2)

    if dog_years > 24:
        owned_dog = int(((dog_years - first_dog_year - second_dog_year) / above_dog_years) + 2)

    
    return [owned_cat, owned_dog]
