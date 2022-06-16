from matplotlib import pyplot as plt
from pandas import DataFrame

from constants import LAGRANGE
from matrix import create_matrix, insert_equations, lu_pivoting, check


def interpolate(xsmpl: [float], ysmpl: [float], n: int, method=LAGRANGE):
    if method == LAGRANGE:
        x = linspace(0, xsmpl[-1], n)
        y = [lagrange_interpolation(xsmpl, ysmpl, xv) for xv in x]
    else:
        x, y = spline_interpolation(xsmpl, ysmpl, n)
    return x, y


def separate_data(df: DataFrame, n: int, equal=True):
    if equal:
        size = df.shape[0] - 1
        indexes = linspace(0, size, n)
        return df.iloc[indexes]
    else:
        return df.sample(n)


def lagrange_interpolation(xsmpl: [float], ysmpl: [float], xv: [float]) -> float:
    m = len(xsmpl)
    n = m - 1
    y = 0
    for i in range(n + 1):
        p = 1
        for j in [nr for nr in range(n + 1) if nr != i]:
            p *= (xv - xsmpl[j]) / (xsmpl[i] - xsmpl[j])
        y += p * ysmpl[i]
    return y


def spline_interpolation(xsmpl: [float], ysmpl: [float], n):
    """
    :param xsmpl:
    :param ysmpl:
    :param n: interpolated values per interval
    :return:
    """
    x = []
    y = []
    intervals = len(xsmpl) - 1
    m = int(n/intervals)
    for i in range(0, len(xsmpl) - 2, 2):
        ax, ay = spline(xsmpl[i:i + 3], ysmpl[i:i + 3], m)
        x += ax
        y += ay
    ax, ay = spline(xsmpl[-3:], ysmpl[-3:], m)
    x += ax[m:]
    y += ay[m:]
    return x, y


# Splajny
# n węzłow, n+1 podprzedziałów, korzystamy ze splajnów 3 stopnia
# n podprzedziałów, 3n niewiadomych (a0, b0, c0, a1 ....)
# dla n wielomianów 2n równań


def get_coefficients(x, y):
    A = create_matrix(8)
    insert_equations(A, x)

    b = [[y[0]], [y[1]], [y[1]], [y[2]], [0], [0], [0], [0]]

    coeff = lu_pivoting(A, b)

    check(A, b, [[c] for c in coeff])
    return coeff


def spline(xsmpl: [float], ysmpl: [float], n):
    coeff = get_coefficients(xsmpl, ysmpl)

    x_0, y_0 = interpolate_spline_in_section(xsmpl[0], xsmpl[1], coeff[:4], n)
    x_1, y_1 = interpolate_spline_in_section(xsmpl[1], xsmpl[2], coeff[4:], n)

    return x_0 + x_1, y_0 + y_1


def interpolate_spline_in_section(x0, x1, coeff, n):
    x_axis = []
    y_axis = []

    split = (x1 - x0) / (n - 1)
    for i in range(n):
        x = x0 + i * split
        xdiff = x - x0

        y = coeff[0] + coeff[1] * xdiff + coeff[2] * xdiff ** 2 + coeff[3] * xdiff ** 3
        x_axis.append(x)
        y_axis.append(y)

    return x_axis, y_axis


def linspace(start, end, n):
    split = (end - start) / (n - 1)
    return [start + i * split for i in range(n)]
