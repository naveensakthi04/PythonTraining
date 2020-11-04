def find_min(lst, start, end):
    min = lst[start]
    min_pos = start
    for i in range(start, end):
        if lst[i] < min:
            min = lst[i]
            min_pos = i
    return min_pos


def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        min_index = find_min(lst, i, length)
        print(lst, min_index)
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


lst = [124, 152, 235, -4587, 456, 357, 85, -45, 3467, 90, -5, 26, 78, 32, 7347, 345]
# lst = [3, 5, 6, 3, 2, 7, 1]
print("\n\nAfter Sorting: ", selection_sort(lst))
