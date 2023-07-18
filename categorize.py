def open_or_senior(data):
    l = list()
    for i, j in data:
        if i>=55 and j>7:
            l.append("Senior")
        else:
            l.append("Open")
    return l

