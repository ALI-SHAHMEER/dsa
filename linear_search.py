print("Linear Search Algorithms")


num = [10,36,82,50,78,36,69]

condition = False
s = 10
i = 0
# print(len(num))

while i != len(num): # loop to iterate in array
    if(num[i] == s): #Condition Checking
        condition = True  
        break        #Exit from loop if found early
    i = i + 1        # increment

if(condition == True):
    print("Found")
else:
    print("Not Found")
