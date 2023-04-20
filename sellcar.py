def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth,t=1):
    m=0
    if startPriceOld>startPriceNew:
        return [0,startPriceOld-startPriceNew]
    else:
        while startPriceOld+m<startPriceNew:
            startPriceNew*=(1-(percentLossByMonth/100))
            startPriceOld*=(1-(percentLossByMonth/100))
            m+=savingperMonth
            t+=1
            if t%2==0:
                percentLossByMonth+=0.5
    return [t-1, round((startPriceOld+m-startPriceNew),0)]


print(nbMonths(2000, 8000, 1000, 1.5))