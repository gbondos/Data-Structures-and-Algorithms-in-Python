# def square_matrix_multiplication(a, b):
#     c = a[:][:]
#     n = len(a)
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 c[i][j] += a[i][k]*b[k][j]
#     for i in range(n):
#         for j in range(n):
#             print(c[i][j] , end = ' ')
#         print("\n", end="")

def matrix_multiplication(M,N):
    # List to store matrix multiplication result
    R = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    # R = M[:][:]


    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]
    print(R)

def main():
    M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

    # Second matrix. N is a list
    N = [[1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]]
    a = [[2, 3], [4, 1]]
    b = [[1, 5], [4, 2]]
    matrix_multiplication(M, N)
main()
