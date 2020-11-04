# 1. Write a Python program to check if a given positive integer is a power of two.
# Input : 4
# Output : True



def isPowerOfTwo(num):
    return num and (not (num & num-1))


num = int(input("Enter a number: "))
result = isPowerOfTwo(num)

if result:
    print("True")
else:
    print("False")

