# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.


def removeAndPrintThirdNumber(numList):
    i = 2
    while i < len(numList):
        print(numList.pop(i), end=" ")
        i = i + 1


numList = input("Enter list of numbers: ")
numList = numList.split(" ")
removeAndPrintThirdNumber(numList)
