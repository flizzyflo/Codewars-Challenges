def two_sum(numbers, target):
    for i,j in enumerate(numbers):
        for k,l in enumerate(numbers):
            if j+l==target and i!=k:
                return [i,k]

    else:
        return "Cant be solved!"

print(two_sum([2,17,2,4], 19))