import math

N = 900
a1 = 8
a2 = -1
a3 = -2
RESIDUUM = 10 ** -9

def init()
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

    b = [math.sin(5 * i) for i in range(N)]

    return A, b

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el if el < 0 else ' ' + str(el), end='\t')
        print('\n')


def convergence_reached(epsilon: [int], residuum):
    return max(epsilon) < residuum


def jacobi(A, b):
    n = len(b)
    x = [1] * n
    epsilon = [math.inf] * n
    k = 0
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

    check(A, b, x)
    return x, k


def gauss_seidl(A, b):
    n = len(b)
    x = [1] * n
    epsilon = [math.inf] * n
    k = 0
    while not convergence_reached(epsilon, RESIDUUM):
        x_prev = x.copy()
        for i in range(len(A)):
            sum = 0
            for j in range(i):
                sum += A[i][j] * x[j]
            for j in range(i + 1, n):
                sum += A[i][j] * x_prev[j]
            x[i] = (b[i] - sum) / A[i][i]
            epsilon[i] = abs((x[i] - x_prev[i]) / x[i])
        k += 1

    check(A, b, x)
    return x, k


def check(A, b, x):
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[i][j] * x[j]
        diff = abs(sum - b[i])
        if diff > RESIDUUM:
            raise ValueError("Błąd! Rozwiązanie nie spełnia układu równań!")


if __name__ == '__main__':
    A, b = init()

    #print_matrix(A)
    x, k = jacobi(A, b)
    print(f"Jacobi {k} iteracji, wyniki: {x}")

    x, k = gauss_seidl(A, b)
    print(f"Gauss-Seidel {k} iteracji, wyniki: {x}")
