# 10. Write a Python program to reverse the digits of an integer.
# Input : 234
# Input : -234
# Output: 432
# Output : -432

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


num = int(input("Enter a number: "))
result = reverseDigits(num)
print(result)
