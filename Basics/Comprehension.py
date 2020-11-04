obj = [letter for letter in "Hello World"]


obj = [i+1 for i in range(10)]

obj = ["Even" for i in range(11) if i % 2 == 0]

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]

obj = {i : "Even" if i % 2 == 0 else "Odd" for i in range(11)}
# print(obj)


# transposed = []
# matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
#
# for i in range(len(matrix[0])):
#     transposed_row = []
#
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)

matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
