from matrix import create_matrix, insert_equations, solve, check

A = create_matrix(8)
b = [[6], [-2], [-2], [4], [0], [0], [0], [0]]
insert_equations(A, [1, 3, 5])
x = solve(A, b)
check(A, b, x)
