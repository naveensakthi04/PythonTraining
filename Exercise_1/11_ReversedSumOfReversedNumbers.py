# 11. Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form.
# Input : 13, 14
# Output : 27
# Note : The result will not be unique for every number for example 31 is a reversed form of several numbers of 13, 130, 1300 etc. Therefore all the leading zeros will be omitted

def reverseDigits(num):
    negFlag = False
    if(num < 0):
        negFlag = True
        num *= -1

    place = 10
    result = 0
    while num > 0:
        temp = num % 10
        result = result * place + temp
        num //= 10

    if(negFlag):
        result *= -1
    return result

def reversedSumOfReversedNumbers(num1, num2):
    return reverseDigits(reverseDigits(num1) + reverseDigits(num2))

num1 = int(input("Enter a reversed number: "))
num2 = int(input("Enter another reversed number: "))
result = reversedSumOfReversedNumbers(num1, num2)
print(result)