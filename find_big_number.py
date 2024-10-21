def find_big_number(simpleArray):
    biggestNumber=simpleArray[0]
    for i in range(1,len(simpleArray)):
        if simpleArray[i] > biggestNumber:
            biggestNumber=simpleArray[i]
    print(biggestNumber)
simpleArray=[5,3,3,3,3,3,3,4]
find_big_number(simpleArray)