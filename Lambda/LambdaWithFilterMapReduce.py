from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

evens = list(filter(lambda a: a % 2 == 0, lst))

doubles = list(map(lambda a: a * 2, evens))

sum = reduce(lambda a, b: a + b, doubles)

print(lst)
print(evens)
print(doubles)
print(sum)