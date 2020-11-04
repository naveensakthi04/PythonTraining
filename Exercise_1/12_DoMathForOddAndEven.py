# 12. Write a Python program where you take any positive integer n, if n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1.
# Input : 12
# Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]

def doMath(num):
    print(num, end=", ")
    if num == 1:
        return
    if num % 2 == 1:
        doMath(num * 3 + 1)
    else:
        doMath(num / 2)


num = int(input("Enter a number: "))
doMath(num)
