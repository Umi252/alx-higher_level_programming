#!/usr/bin/python3
matrix_module = __import__('6-print_matrix_integer')
print_matrix_integer = matrix_module.print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
