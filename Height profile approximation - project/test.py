import re

import mplcyberpunk
import pandas as pd
from matplotlib import pyplot as plt

from constants import DISTANCE, HEIGHT, LAGRANGE
from utils import separate_data, lagrange_interpolation, linspace, interpolate


class TestMethodsObject:

    def __init__(self, files, samples, show=True):
        self.FILES = files
        self.SAMPLES = samples
        self.index = 1
        self.show = show

    def test_method(self, samples, equal_space=True, interpolation_method=LAGRANGE, interpoated_points=500):
        for file in self.FILES:
            df = pd.read_csv(f'2018_paths/{file}.csv')
            x_org = df[DISTANCE]
            y_org = df[HEIGHT]
            for smpl in samples:
                sample = separate_data(df, smpl, equal_space)
                x_samples = list(sample[DISTANCE])
                y_samples = list(sample[HEIGHT])

                interpolated_x, interpolated_y = interpolate(x_samples, y_samples, interpoated_points, interpolation_method)

                description, title = self.get_plot_title_and_description(interpolation_method, file, smpl, equal_space)

                plot = self.plot(x_org, y_org, x_samples, y_samples, interpolated_x, interpolated_y, title,
                                 description)
                random = "eq" if equal_space else "rand"
                plot.show() if self.show else plot.savefig(f"charts/{interpolation_method}/{file}-{random}-{smpl}-samples.png")
                plot.close()
                self.index += 1

    @staticmethod
    def plot(org_x, org_y, probes_x, probes_y, interpolated_x, interpolated_y, title, description):
        plt.figure(figsize=(11, 5))
        plt.plot(org_x, org_y, label="Oryginalny wykres")
        plt.plot(interpolated_x, interpolated_y, label="Funkcja interpolacyjna")
        plt.plot(probes_x, probes_y, 'o', markersize=12, label="Próbki", color="lime")
        plt.title(title, fontsize=20, **{'fontname':'Verdana'})
        plt.legend(prop={'size': 13})
        plt.xlabel(DISTANCE + '\n'+description, fontsize=13)
        plt.ylabel(HEIGHT, fontsize=13)
        plt.tight_layout()

        mplcyberpunk.make_lines_glow()
        return plt

    def get_plot_title_and_description(self, method_name, file, smpl, equal):
        filename = re.sub(r"(\w)([A-Z])", r"\1 \2", file)
        title = f"{method_name} dla {filename}, ilość próbek = {smpl}"
        probes = "równo odległych" if equal else "losowo wybranych"
        description = f"\nwyk. {self.index} prezentuje przeprowadzenie interpolacji metodą Lagrange'a\n dla {smpl} {probes} " \
                      f"próbek z pliku {file}.csv "
        return description, title
