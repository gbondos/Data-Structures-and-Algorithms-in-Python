def matrix_subtraction(a, b):
    # This subtracts matrix b from matrix a
    c = a[:][:]
    for i in range(len(a)):
        for j in range(len(b)):
            c[i][j] = a[i][j] - b[i][j]
    print (c)

def main():
    a = [[5, 6], [3, 4]]
    b = [[1, 2], [2, 1]]
    matrix_subtraction(a, b)
main()
