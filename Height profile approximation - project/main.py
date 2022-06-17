import re

import mplcyberpunk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

from constants import DISTANCE, HEIGHT, FILES, SAMPLES, SPLINE, LAGRANGE
from matrix import create_matrix, print_matrix, insert_equations, multiply, lu_pivoting
from test import TestMethodsObject
from utils import separate_data, lagrange_interpolation, spline

# set font
plt.rcParams['font.family'] = 'Roboto Mono'

plt.style.use("cyberpunk")
test = TestMethodsObject(FILES, SAMPLES, False)
test.test_method([4, 8, 14], True, LAGRANGE, 500)
test.test_method([8, 20, 40], True, SPLINE, 1000)

test.test_method([8], False, LAGRANGE, 500)
test.test_method([20], False, SPLINE, 1000)
