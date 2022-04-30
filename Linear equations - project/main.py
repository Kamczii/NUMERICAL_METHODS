import math
import time

import matplotlib.pyplot as plt

RESIDUUM = 10 ** -9
ITERATION_LIMIT = 500

FIXED_N = 974


def init_a(N: int = FIXED_N) -> ([[float]], [float]):
    a1 = 8
    a2 = a3 = -1

    A = create_matrix(N, a1, a2, a3)

    b = [math.sin(5 * i) for i in range(N)]

    return A, b


def init_b(N: int = FIXED_N) -> ([[float]], [float]):
    a1 = 3
    a2 = a3 = -1

    A = create_matrix(N, a1, a2, a3)

    b = [math.sin(5 * i) for i in range(N)]

    return A, b


def create_matrix(N, a1, a2, a3):
    A = []
    for i in range(N):
        A.append([])
        for j in range(N):
            if i == j:
                A[i].append(a1)
            elif i - j == 1 or i - j == -1:
                A[i].append(a2)
            elif i - j == 2 or i - j == -2:
                A[i].append(a3)
            else:
                A[i].append(0)
    return A


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(round(el, 2) if el < 0 else ' ' + str(round(el, 2)), end='\t')
        print('\n')


def convergence_reached(epsilon: [int], residuum):
    return max(epsilon) < residuum


def create_identity_matrix(n):
    return create_matrix(n, 1, 0, 0)


def swap_rows(matrix: [[]], row1: int, row2: int):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return


def check(A, b, x):
    N = len(b)
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[i][j] * x[j]
        diff = abs(sum - b[i])
        if diff > RESIDUUM:
            raise ValueError(f"Błąd! Rozwiązanie nie spełnia układu równań! Różnica: {diff} dla x{i}")


def highest_diff(A, b, x):
    N = len(b)
    diffs = []
    for i in range(N):
        summation = 0
        for j in range(N):
            summation += A[i][j] * x[j]
        diffs.append(abs(summation - b[i]))
    return max(diffs)


def upper(matrix):
    U = [[] for r in matrix]
    for i, row in enumerate(matrix):
        for j, a in enumerate(row):
            if j > i:
                U[i].append(a)
            else:
                U[i].append(0)
    return U


def lower(matrix):
    L = [[] for r in matrix]
    for i, row in enumerate(matrix):
        for j, a in enumerate(row):
            if j < i:
                L[i].append(a)
            else:
                L[i].append(0)
    return L


def jacobi(A, b):
    n = len(b)  # dimension of matrix
    x = [1] * n  # vector of results
    epsilon = [math.inf] * n  # approximations
    k = 0  # iterations
    while not convergence_reached(epsilon, RESIDUUM):
        x_prev = x.copy()
        for i, row in enumerate(A):  # dla każdego wiersza
            summation = 0
            for j, a in enumerate(row):
                if j != i:
                    summation += a * x_prev[j]
            x[i] = (b[i] - summation) / A[i][i]
            epsilon[i] = abs((x[i] - x_prev[i]) / x[i])
        k += 1
        if k > ITERATION_LIMIT:
            print("Metoda Jacobiego nie zbiega się osiągnięto limit iteracji!")
            return [], math.inf
    check(A, b, x)
    return x, k


def gauss_seidel(A, b):
    n = len(b)
    x = [1] * n
    epsilon = [math.inf] * n
    k = 0
    while not convergence_reached(epsilon, RESIDUUM):
        x_prev = x.copy()
        for i, (row, bv) in enumerate(zip(A, b)):
            summation = 0
            for j, a in enumerate(row[:i]):
                summation += a * x[j]
            for j, a in enumerate(row[i + 1:], start=i + 1):
                summation += a * x_prev[j]
            x[i] = (bv - summation) / A[i][i]
            epsilon[i] = abs((x[i] - x_prev[i]) / x[i])
        k += 1
        if k > ITERATION_LIMIT:
            print("Metoda Gaussa-Seidla nie zbiega się osiągnięto limit iteracji!")
            return [], math.inf
    check(A, b, x)
    return x, k


def lu_factorization(matrix):
    n = len(matrix)
    L = create_identity_matrix(n)
    U = matrix.copy()
    for i in range(n):
        for j in range(i + 1, n):
            l = U[i][j] / U[i][i]
            L[j][i] = l
            U[j] = [a1 - l * a2 for (a1, a2) in zip(U[j], U[i])]
    return L, U


def plu_factorization(matrix):
    n = len(matrix)
    L = create_identity_matrix(n)
    U = matrix.copy()
    P = L.copy()
    for i in range(n):
        k = i
        while U[i][i] == 0:
            swap_rows(U, i, k + 1)
            swap_rows(P, i, k + 1)
            k += 1
        for j in range(i + 1, n):
            l = U[i][j] / U[i][i]
            L[j][i] = l
            U[j] = [a1 - l * a2 for (a1, a2) in zip(U[j], U[i])]
    return L, U


# [L][y]=[b]
def forward_substitution(L, b):
    n = len(b)
    y = [b[0] / L[0][0]]
    for i in range(1, n):
        summation = 0
        for j in range(i):
            summation += L[i][j] * y[j]
        y.append((b[i] - summation) / L[i][i])
    return y


# [U][x]=[y]
def backward_substitution(U, y):
    n = len(y)
    x = [yv / U[i][i] for i, yv in enumerate(y)]
    for i in range(n - 1, -1, -1):
        summation = 0
        for j in range(i + 1, n):
            summation += U[i][j] * x[j]

        x[i] = (y[i] - summation) / U[i][i]
    return x


def lu(A, b):
    L, U = plu_factorization(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    check(A, b, x)
    return x


def task1_2():
    A, b = init_a()
    start = time.perf_counter()
    x, k = jacobi(A, b)
    end = time.perf_counter()
    print(f"Zad2. Jacobi {k} iteracji w czasie {end - start}, wyniki: {x}")

    start = time.perf_counter()
    x, k = gauss_seidel(A, b)
    end = time.perf_counter()
    print(f"Zad2. Gauss-Seidel {k} iteracji w czasie {end - start}, wyniki: {x}")
    return


def task3():
    A, b = init_b()
    start = time.perf_counter()
    x, k = jacobi(A, b)
    end = time.perf_counter()
    print(f"Zad3. Jacobi {k} iteracji w czasie {end - start}s, wyniki: {x}")

    start = time.perf_counter()
    x, k = gauss_seidel(A, b)
    end = time.perf_counter()
    print(f"Zad3. Gauss-Seidel {k} iteracji w czasie {end - start}s, wyniki: {x}")
    return


def task4():
    A, b = init_b()
    start = time.perf_counter()
    x = lu(A, b)
    end = time.perf_counter()
    diff = highest_diff(A, b, x)
    print(f"Zad4. Faktoryzacja LU zajęła {end - start}s, norma z residuum wynosi {diff}, wyniki: {x} ")
    return


def task5():
    N = [100, 500, 1000, 2000]

    jacobi_method = []
    gauss_seidel_method = []
    lu_factorization_method = []

    for n in N:
        A, b = init_a(n)
        start = time.perf_counter()
        jacobi(A, b)
        end = time.perf_counter()
        jacobi_method.append(end - start)

        start = time.perf_counter()
        gauss_seidel(A, b)
        end = time.perf_counter()
        gauss_seidel_method.append(end - start)

        start = time.perf_counter()
        lu(A, b)
        end = time.perf_counter()
        lu_factorization_method.append(end - start)

    plt.title("Wykres czasu działania metod iteracyjnych")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas działania [sek]")
    plt.plot(N, jacobi_method, label='Jacobi')
    plt.plot(N, gauss_seidel_method, label='Gauss-Seidel')
    plt.plot(N, lu_factorization_method, label='Faktoryzacja LU')
    plt.legend()
    plt.show()
    plt.savefig('wykres.png')


if __name__ == '__main__':
    task1_2()
    task3()
    task4()
    task5()
