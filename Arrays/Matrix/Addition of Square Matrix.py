
def matrix_addition(matrix_a, matrix_b):
    c =matrix_a[:][:]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b)):
            c[i][j]  = matrix_a[i][j] + matrix_b[i][j]
    print(c)

def main():
    a = [[0, 0], [1, 3]]
    b = [[3, 2], [5, 1]]
    matrix_addition(a, b)
main()
