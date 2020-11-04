# 6. Write a Python program to find missing numbers from a list.
# Input : [1,2,3,4,6,7,10]
# Output : [5, 8, 9]


def missingNumbers(numList):

    result = []
    x = int(numList[0])
    i = 0
    length = len(numList)

    while i < length:
        if int(numList[i]) == x:
            i = i + 1
        else:
            result.append(x)
        x = x + 1
    return result

numList = input("Enter list of numbers: ")
numList = numList.split(" ")
result = missingNumbers(numList)
for i in result:
    print(i, end=" ")
