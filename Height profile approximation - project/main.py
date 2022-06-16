import re

import mplcyberpunk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from constants import DISTANCE, HEIGHT, FILES
from matrix import create_matrix, print_matrix, insert_equations, multiply, lu_pivoting, solve
from utils import separate_data, lagrange

index = 1

plt.style.use("cyberpunk")

files = FILES
samples = [4, 8, 14]

# Lagrange
# for file in files:
#     df = pd.read_csv(f'2018_paths/{file}.csv')
#     for smpl in samples:
#         sample = separate_data(df, smpl, True)
#
#         distance = list(sample[DISTANCE])
#         height = list(sample[HEIGHT])
#
#         x = np.linspace(0, df[DISTANCE].iloc[-1], 500)
#
#         title = re.sub(r"(\w)([A-Z])", r"\1 \2", file)
#         plt.figure(figsize=(15, 9))
#         plt.plot(df[DISTANCE], df[HEIGHT], label="Originalny wykres")
#         plt.plot(distance, height, 'o', markersize=12, label="Próbki", color="lime")
#         plt.plot(x, lagrange(distance, height, x), label="Funkcja interpolacyjna")
#         plt.title(f"Lagrange dla {title}, ilość próbek = {smpl}", fontsize=25)
#         plt.legend(prop={'size': 16})
#         plt.figtext(0.5, 0.001, f"wyk. {index} prezentuje przeprowadzenie interpolacji metodą Lagrange'a dla {smpl} pr"
#                                f"óbek z pliku {file}.csv", wrap=True, horizontalalignment='center', fontsize=18)
#         plt.show()
#         index += 1
#         #plt.savefig(f"charts/lagrange/{file}-{smpl}-samples.png")

matrix = create_matrix(8)
insert_equations(matrix, [1, 3, 5])

print(solve(matrix,  [[6],[-2],[-2],[4],[0],[0],[0],[0]]))