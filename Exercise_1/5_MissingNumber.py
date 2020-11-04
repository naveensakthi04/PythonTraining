# 5. Write a Python program to find a missing number from a list.
# Input : [1,2,3,4,6,7,8]
# Output : 5

def missingNumber(numList):

    i = int(numList[0])

    for num in numList:
        if(i != int(num)):
            return i
        i = i + 1
    return -1


numList = input("Enter list of numbers: ")
numList = numList.split(" ")
result = missingNumber(numList)
print(result)
