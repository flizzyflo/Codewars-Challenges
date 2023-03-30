def stray(arr):
    for i in arr:
        if arr.count(i)==1:
            return i
        else:
            pass

print(stray([1,2,1,1,1]))