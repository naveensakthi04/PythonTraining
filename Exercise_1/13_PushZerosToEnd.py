# 13. Write a Python program to push all zeros to the end of a list.
# Input : [0,2,3,4,6,7,10]
# Output : [2, 3, 4, 6, 7, 10, 0]

def pushZerosToEnd(numbers):

    i = 0
    length = len(numbers)
    while i < length:
        if numbers[i] == 0:
            numbers.pop(i)
            numbers.append(0)
            length -= 1
        else:
            i += 1

    return numbers

numList = input("Enter list of numbers: ")
numList = numList.split(" ")
numbers = list()

for i in numList:
    numbers.append(int(i))
result = pushZerosToEnd(numbers)
print(result)
