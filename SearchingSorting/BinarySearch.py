def binary_search(lst, n, low, high):
    mid = int((low + high) / 2)
    if low >= high:
        return 0
    if lst[mid] == n:
        return mid + 1
    elif lst[mid] < n:
        binary_search(lst, n, mid + 1, high)
    elif lst[mid] > n:
        binary_search(lst, n, low, mid - 1)



lst = [12, 15, 23, 45, 46, 57, 85, 90, 346, 7347, 34513]
key = int(input("Enter the number to be searched: "))
result = binary_search(lst, key, 0, len(lst))
if result:
    print("Found at {}".format(result))
else:
    print("Sorry, Not found!")
