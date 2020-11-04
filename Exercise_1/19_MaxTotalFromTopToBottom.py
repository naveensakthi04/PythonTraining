# 19. Write a Python program to find the maximum total from top to bottom of the triangle below.
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 25.
#    3
#   4 6
#  2 7 6
# 8 5 9 3   OUTPUT 25




def findMaxSum(numbers):
    maxi = -99999
    for i in numbers:
        sum = 0
        for j in i:
            sum += int(j)
        if sum > maxi:
            maxi = sum

    return maxi


# lines = []
# print("Input:")
# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
lines = ['   100', '  -4 6', ' 2 78 -60', '80 5 9 3']

numbers = []
for i in lines:
    i = i.strip()
    i = i.split(" ")
    numbers.append(i)

result = findMaxSum(numbers)
print(result)