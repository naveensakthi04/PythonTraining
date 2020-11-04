import math


def maxPrimeFactor(num):
    result = -1
    while num % 2 == 0:
        result = 2
        num /= 2

    for i in range(int(math.sqrt(num))):
        while num % i == 0:
            result = i
            num /= i

    if num > 2:
        result = num

    return result


num = int(input("Enter a number: "))
result = maxPrimeFactor(num)
print(result)