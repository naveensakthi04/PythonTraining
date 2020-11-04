def bubble_sort(lst):
    length = len(lst)
    print(length)
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(lst)
    return lst


lst = [124, 152, 235, -4587, 456, 357, 85, -45, 3467, 90, -5, 26, 78, 32, 7347, 345]
# lst = [3, 5, 6, 3, 2, 7, 1]
print("\n\nAfter Sorting: ", bubble_sort(lst))
