def linear_search(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i + 1
    return 0


lst = [124, 152, 235, 4587, 456, 357, 85, 45, 3467, 90, 5, 26, 78, 32, 7347, 345]
key = int(input("Enter the number to be searched: "))
result = linear_search(lst, key)
if result:
    print("Found at {}".format(result))
else:
    print("Sorry, Not found!")
