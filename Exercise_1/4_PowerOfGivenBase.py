# 4. Write a Python program to check if a number is a power of a given base.
# Input : 128,2
# Output : True

import math


def isPowerOfGivenBase(num, base):
    num = math.log(num) / math.log(base)
    return math.ceil(num) == math.floor(num)



input_value = input("Enter a number,base: ")
input_value = input_value.split(",")
num = int(input_value[0])
base = int(input_value[1])

result = isPowerOfGivenBase(num, base)

if result:
    print("True")
else:
    print("False")

