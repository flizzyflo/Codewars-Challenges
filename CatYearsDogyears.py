def human_years_cat_years_dog_years(human_years: int) -> list[int]:
    
    first_year_cat, first_year_dog = 15, 15
    sec_year_cat, sec_year_dog = 9, 9
    after_sec_cat, after_sec_dog = 4, 5

    if human_years == 0:
        return [0, 0, 0]

    elif human_years == 1:
        return [human_years, first_year_cat, first_year_dog]
    
    elif human_years == 2:
        return [human_years, first_year_cat + sec_year_cat, first_year_dog + sec_year_dog]

    else:
        multiplier = human_years - 2
        return [human_years, 24 + multiplier * after_sec_cat, 24 + multiplier * after_sec_dog]

  