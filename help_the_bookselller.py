def stock_list(list_of_art: list[str], list_of_cat: list[str]) :
    
    cat_values = {category: 0 for category in list_of_cat}
    
    for article in list_of_art:
        cur_key = article[0]
        
        if cur_key not in list_of_cat:
            continue
        
        cat_values[cur_key] += int(article.split()[1])
    

    return transform_string(cat_values)

b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]

def transform_string(d: dict[str, int]) -> str:

    res_str = ""
    for key, value in d.items():
        if res_str == "":
            res_str += f"({key} : {value})"

        else:
            res_str +=  f" - ({key} : {value})"

    return res_str

print(stock_list(b, c))