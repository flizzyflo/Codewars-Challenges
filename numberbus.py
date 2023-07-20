def number(bus_stops):
    passenger=0
    if passenger>=0:
        for etr, out in bus_stops:
            passenger=passenger+etr-out
        return passenger
    else:
        return 0

print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))