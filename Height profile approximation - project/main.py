import re

import mplcyberpunk
import pandas as pd
import matplotlib.pyplot as plt

from constants import DISTANCE, HEIGHT, FILES, SAMPLES, SPLINE, LAGRANGE
from matrix import create_matrix, print_matrix, insert_equations, multiply, lu_pivoting
from test import TestMethodsObject
from utils import separate_data, lagrange_interpolation, spline

plt.style.use("cyberpunk")

test = TestMethodsObject(FILES, SAMPLES, True)
test.test_method(LAGRANGE, 500)
test.test_method(SPLINE, 100)

