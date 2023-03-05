
def namelist(names: list) -> str:
    
    
    def create_result_string(names: str) -> str:
        iterator = 1
        result_string = str()
        for name in names:  
            
            if iterator == len(names):
                result_string += " & " + name["name"]
                return result_string

            if iterator == len(names) - 1:
                result_string += name["name"]
            
            else:
                result_string += name["name"] + ", "
        
            iterator += 1

    if len(names) == 0:
        return f''

    if len(names) == 1:
        return f'{names[0]["name"]}'

    else:

        return create_result_string(names)
    



print(namelist([{"name" : "Bart"}]))