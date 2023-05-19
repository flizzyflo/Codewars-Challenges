
def queue_time(customers: list, number_of_tills: int) -> int:

    result = 0
    time_left = int()

    if number_of_tills == 1:
        return sum(customers)

    elif number_of_tills >= len(customers):
        return max(customers)

    else:
        
        while customers != []:

            if len(customers) < number_of_tills:
                 time_left = max(customers)

            time_left = max(customers[:number_of_tills])
            
            result += min(customers[:number_of_tills])
            time_left -= min(customers[:number_of_tills])

            start_index = 0
            temp = min(customers[:number_of_tills])
            for customer in customers[:number_of_tills]:
                
                customers[start_index] -= temp
                start_index += 1

            customers.remove(min(customers[:number_of_tills]))

        
        else: 
            return result
            


print(queue_time([50, 43, 26, 43, 1, 20, 34, 34, 33, 49, 48, 49] , 4))

#elegangter

# def queue_time(customers, n):
#     tills = [0 for i in range(n)]

#     for time in customers:
#         min_index = tills.index(min(tills))
#         tills[min_index] += time

#     return max(tills)