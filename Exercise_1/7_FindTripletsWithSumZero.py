# 7. Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# Input : [-1,0,1,2,-1,-4]
# Output : [[-1, -1, 2], [-1, 0, 1]]
# Note : Find the unique triplets in the array.

def findTripletsWithSumZero(numbers):
    n = len(numbers)

    result = set()

    numbers.sort()

    for i in range(0, n - 1):
        left = i + 1
        right = n - 1
        x = numbers[i]
        temp = list()

        while left < right:
            temp.clear()
            sum = numbers[left] + numbers[right] + x


            if sum == 0:
                # print(numbers[left], numbers[right], x)
                temp.append(numbers[left])
                temp.append(numbers[right])
                temp.append(x)
                left = left + 1
                right = right - 1

            elif sum > 0:
                right = right - 1
            else:
                left = left + 1
            if not (len(temp) == 0):
                result.add(tuple(temp))

    return result


numList = input("Enter list of numbers: ")
numList = numList.split(",")
numbers = list()
for i in numList:
    numbers.append(int(i))
result = findTripletsWithSumZero(numbers)
print(result)
