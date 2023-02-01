def number(lines):
    d=[]
    for n,l in enumerate(lines):
        string=str(n+1)+": "+l
        d.append(string)
    return d

print(number(["a", "b", "c"]))