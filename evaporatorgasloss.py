def evaporator(content, evap_per_day, threshold, n=0):

    con = content
    while con/content > threshold/100:
        con = con*(1-evap_per_day/100)
        n += 1
    return n

print(evaporator(10,10,10))