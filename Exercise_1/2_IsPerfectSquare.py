# 2. Write a Python program to check if a number is a perfect square.
# Input : 9
# Output : True


import math


def isPerfectSquare(num):
    num = math.sqrt(num)
    return math.ceil(num) == math.floor(num)


num = int(input("Enter a number: "))
result = isPerfectSquare(num)

if result:
    print("True")
else:
    print("False")

