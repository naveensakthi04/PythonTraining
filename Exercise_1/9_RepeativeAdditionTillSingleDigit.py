# 9. Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
# Input : 48
# Output : 3
# For example given number is 59, the result will be 5.
# Step 1: 5 + 9 = 14
# Step 1: 1 + 4 = 5


def repeativeAdditionTillSingleDigit(num):
    if num < 10:
        return num

    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return repeativeAdditionTillSingleDigit(sum)



num = int(input("Enter a number: "))
result = repeativeAdditionTillSingleDigit(num)
print(result)
