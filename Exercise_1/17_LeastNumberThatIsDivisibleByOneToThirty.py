# 17. Write a Python program to find the smallest positive number that is evenly divisible by all of the numbers from 1 to 30.
# Result: 2329089562800.0


# The main steps of our algorithm are:
#
# Initialize ans = arr[0].
# Iterate over all the elements of the array i.e. from i = 1 to i = n-1
# At the ith iteration ans = LCM(arr[0], arr[1], …….., arr[i-1]).
# This can be done easily as LCM(arr[0], arr[1], …., arr[i]) = LCM(ans, arr[i]).
# Thus at i’th iteration we just have to do ans = LCM(ans, arr[i]) = ans x arr[i] / gcd(ans, arr[i])

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(n):
    result = 1

    for i in range(2, 30):
        result = (i * result) / (gcd(i, result))
    return result


num = int(input("Enter the number: "))
result = lcm(num)
print(result)