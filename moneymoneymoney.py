def calculate_years(principal, interest, tax, desired):
    years=0
    summe=principal
    while summe<desired:
        summe=summe+(summe*interest)*(1-tax)
        years+=1
    return years

print(calculate_years(20000, 0.002, 0.25, 50000))