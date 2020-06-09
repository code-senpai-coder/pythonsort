import time




array = [1,2,5,3,6,9,8,7,4,5,6,3,2,5,4,5,8,6,5,4,1,5,65,2,2,5,2,5,2,5,6,9,8,55,4,8,5,8,5,8,5,5,8,9,6,9,6,9,8,7,4,5,6,6,9,8,5,2,6,8,8,2,6,8,5,6,3]
lenArr = len(array) 
operationCountLimit = len(array) - 1

firstIndex = 0
secondIndex = 1



operationCount = 0
curtime = time.time()
while True:
    if(array[firstIndex] > array[secondIndex]):

        array[firstIndex] , array[secondIndex] = array[secondIndex], array[firstIndex]
    elif(array[firstIndex] <= array[secondIndex]):

        operationCount +=1
        pass
    firstIndex += 1
    secondIndex += 1 

    if (secondIndex == lenArr):
        if(operationCount >= operationCountLimit):
            print(f"Your sorted array is {array}")
            comptime = time.time()
            timetocompltet = (comptime - curtime)
            print(f"This operation has taken {timetocompltet} seconds")
            time.sleep(99999)
            break
        firstIndex = 0
        secondIndex = 1
        operationCount = 0



    
    

    