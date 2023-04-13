
def xbonacci(input_list: list[int], desired_length: int) -> list[int]:

    counter, list_count = len(input_list), 0

    while counter < desired_length:
        
        input_list.append(sum(input_list[list_count:len(input_list) + list_count]))
        list_count += 1
        counter += 1

    return input_list[:desired_length]
