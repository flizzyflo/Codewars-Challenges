def count(string):
    di=dict()
    if string:
        for l in string:
            if l in di:
                di[l]+=+1
            else:
                di[l]=1
        return di
    else:
        return {}

print(count("aertaaatwt"))