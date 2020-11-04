# 15. Write a Python program to compute the sum of all the multiples of 3 or 5 below 200.
# All the natural numbers below 12 that are multiples of 3 or 5, we get 3, 5, 6, 9 and 10. The sum of these multiples is 33.

n = 200
def sumOfMulitples(base):
    i = 1
    sum = 0
    for i in range(n):
        if i % base == 0:
            sum += i
    return sum

# AP formula
# n /= d;
#
#     return (n) * (1 + n) * d / 2;

print(sumOfMulitples(3) + sumOfMulitples(5) - sumOfMulitples(3 * 5))
