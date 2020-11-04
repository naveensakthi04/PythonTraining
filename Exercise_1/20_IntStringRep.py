# 20. Write a Python program that takes a string and encode it that the amount of symbols would be represented by integer and the symbol.
# For example, the string "AAAABBBCCDAAA" would be encoded as "4A3B2C1D3A"
# Sample Output:
# 4A3B2C1D3A

def intStringRep(s):

    i = 0
    while i < len(s):
        count = 1
        j = i + 1
        while (j < len(s)) and (s[i] == s[j]):
            count += 1
            j += 1
        newstring = str(count) + s[i]
        s = s[:i] + newstring + s[j :]
        i += 2
    return s


s = input("Enter a string: ")
result = intStringRep(s)
print(result)