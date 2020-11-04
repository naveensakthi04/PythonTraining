# 8. Write a Python program to find the single number in a list that doesn't occur twice.
# Input : [5, 3, 4, 3, 4]
# Output : 5

def numberThatExistsNotTwice(numList):
    dictionary = dict()
    for i in numList:
        if i in dictionary:
            dictionary.update({i: dictionary.get(i)+1})
        else:
            dictionary.update({i: 1})

    for k, v in dictionary.items():
        if v != 2:
            return k



numList = input("Enter list of numbers: ")
numList = numList.split(",")
numbers = list()
for i in numList:
    numbers.append(int(i))

result = numberThatExistsNotTwice(numbers)
print(result)