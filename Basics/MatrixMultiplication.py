def create_matrix():
    rows = int(input("Enter the number of rows for matrix: "))
    columns = int(input("Enter the number of columns for matrix: "))
    matrix = get_input(rows, columns)
    return matrix


def get_input(rows, columns):
    matrix = []
    print("Enter the matrix values: ")
    for i in range(rows):
        temp_row = []
        for j in range(columns):
            temp_row.append(int(input()))
        matrix.append(temp_row)
    return matrix


def multiply(m1, m2):
    result = []
    for i in range(len(m1)):
        temp_row = []
        for j in range(len(m2[0])):
            temp_row.append(0)
        result.append(temp_row)

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result


def print_matrix(matrix):
    print("-------------------------")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    print("-------------------------")


# main

matrix_one = create_matrix()
matrix_two = create_matrix()

print_matrix(matrix_one)
print_matrix(matrix_two)

if len(matrix_one[0]) == len(matrix_two):
    print_matrix(multiply(matrix_one, matrix_two))
else:
    print("Sorry, multiplication of these two matrices is not possible.")