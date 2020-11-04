def calc(n):
    result = 0
    for i in range(1, 5):
        result += int(n*i)
    return result


# Driver code
digit = input("Enter a digit: ")[0]
result = calc(digit)
print(result)
