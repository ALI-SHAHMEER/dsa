print("Binary Search Algorithms")

s = 36
num = [10,20,28,36,57,64,71,86,99]
condition = False

middle = round(len(num)/2) #Calculate middle and rounding off

if(s > num[middle]): # if number greater than array[middle] then go with this condition
    while middle != len(num): # loop to iterate in array
        if(s == num[middle]): #Condition Checking
            condition = True
            break             #Exit from loop if found early
        middle = middle + 1   #Increment
else:
    while middle != 0:        # loop to iterate in array
        if(s == num[middle]): #Condition Checking 
            condition = True  
            break             #Exit from loop if found early
        middle = middle - 1   #Decrement

if(condition == True):
    print("Found")
else:
    print("Not Found")