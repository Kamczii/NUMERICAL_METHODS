import copy
import math

RESIDUUM = 10 ** -9
ITERATION_LIMIT = 500

FIXED_N = 974


def create_matrix(N):
    return [[0.0 for _ in range(N)] for _ in range(N)]


def insert_equations(matrix: list[list], x: list[float]):
    h0 = x[1] - x[0]
    h1 = x[2] - x[1]

    matrix[0][0] = 1  # a0 = f (x0)

    matrix[1][4] = 1  # a1 = f (x1)

    matrix[2][0] = 1
    matrix[2][1] = h0
    matrix[2][2] = h0 ** 2
    matrix[2][3] = h0 ** 3

    matrix[3][4] = 1
    matrix[3][5] = h1
    matrix[3][6] = h1 ** 2
    matrix[3][7] = h1 ** 3

    matrix[4][1] = 1
    matrix[4][2] = 2 * h0
    matrix[4][3] = 3 * h0 ** 2
    matrix[4][5] = -1

    matrix[5][2] = 2
    matrix[5][3] = 6 * h0
    matrix[5][6] = -2

    matrix[6][2] = 2

    matrix[7][6] = 2
    matrix[7][7] = 6 * h1

    for row in matrix:
        for i, el in enumerate(row):
            row[i] = float(el)


def print_matrix(matrix):
    for i, row in enumerate(matrix):
        for el in row:
            print(round(el, 2) if el < 0 else ' ' + str(round(el, 2)), end='\t')
        print('\n')
    print('\n------------------------------------------------\n')


def convergence_reached(epsilon: [int], residuum):
    return max(epsilon) < residuum


def create_identity_matrix(n) -> list[list]:
    matrix = create_matrix(n)
    for i in range(n):
        matrix[i][i] = 1.0
    return matrix


def swap_rows(matrix: list[list], row1: int, row2: int):
    if row1 != row2:
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def check(A, b, x):
    N = len(b)
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[i][j] * x[j]
        diff = abs(sum - b[i][0])
        if diff > RESIDUUM:
            raise ValueError(f"Błąd! Rozwiązanie nie spełnia układu równań! Różnica: {diff} dla x{i}")


def multiply(A, B):
    A_rows = len(A)
    A_columns = len(A[0])
    B_rows = len(B)
    B_columns = (len(B[0]))
    assert  A_columns == B_rows

    C = [[0 for _ in range(B_columns)] for _ in range(A_rows)]

    for i in range(A_rows):
        for j in range(B_columns):
            sum = 0
            for k in range(B_rows):
                sum += A[i][k]*B[k][j]
            C[i][j] = sum
    return C


def find_pivot(U, k):
    row_idx = k
    for i in range(k, len(U)):
        if abs(U[i][k]) > abs(U[row_idx][k]):
            row_idx = i
    return row_idx


def lu_pivoting(matrix, b):
    size = len(matrix)
    A = matrix
    L = create_identity_matrix(size)
    P = create_identity_matrix(size)
    U = copy.deepcopy(A)

    for k in range(size - 1):
        # print(f"k={k}")
        # print_matrix(U)
        pivot_idx = find_pivot(U, k)

        swap_rows(P, k, pivot_idx)
        swap_rows(L, k, pivot_idx)
        swap_rows(U, k, pivot_idx)

        for j in range(k + 1, size):
            factor = U[j][k] / U[k][k]
            L[j][k] = factor
            for i in range(k, size):
                U[j][i] -= factor * U[k][i]

    print_matrix(L)

    b = multiply(P, b)
    y = [0 for _ in range(size)]
    # Forward substitution Ly = b
    for row in range(size):
        s = 0
        for col in range(0, row):
            s += L[row][col] * y[col]
        y[row] = b[row][0] - s

    x = [0 for _ in range(size)]
    for row in range(size - 1, -1, -1):  # Ux = y
        s = 0
        for col in range(size - 1, -1, -1):
            s += U[row][col] * x[col]
        x[row] = (y[row] - s) / U[row][row]
    return x


def solve(A, b):
    return lu_pivoting(A, b)