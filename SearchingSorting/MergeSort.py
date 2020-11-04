def merge(lst, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    l = [0] * n1
    r = [0] * n2


    for i in range(n1):
        l[i] = lst[start + i]
    for j in range(0, n2):
        r[j] = lst[mid + 1 + j]

    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            lst[k] = l[i]
            i += 1
        else:
            lst[k] = r[j]
            j += 1
        k += 1

    while i < n1:
        lst[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        lst[k] = r[j]
        j += 1
        k += 1

    print(lst)

def merge_sort(lst, start, end):
    if (start < end):
        mid = int((start + end - 1) / 2)

        merge_sort(lst, start, mid)
        merge_sort(lst, mid + 1, end)
        merge(lst, start, mid, end)


lst = [124, 152, 235, -4587, 456, 357, 85, -45, 3467, 90, -5, 26, 78, 32, 7347, 345]
# lst = [3, 5, 6, 3, 2, 7, 1]
merge_sort(lst, 0, len(lst)-1)
print("\n\nAfter Sorting: ", lst)
