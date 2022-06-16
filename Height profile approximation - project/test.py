import re

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

    def test_method(self, interpolation_method=LAGRANGE, interpoated_points=500):
        for file in self.FILES:
            df = pd.read_csv(f'2018_paths/{file}.csv')
            x_org = df[DISTANCE]
            y_org = df[HEIGHT]
            for smpl in self.SAMPLES:
                sample = separate_data(df, smpl, True)
                x_samples = list(sample[DISTANCE])
                y_samples = list(sample[HEIGHT])

                interpolated_x, interpolated_y = interpolate(x_samples, y_samples, interpoated_points, interpolation_method)

                description, title = self.get_plot_title_and_description(interpolation_method, file, smpl)

                plot = self.plot(x_org, y_org, x_samples, y_samples, interpolated_x, interpolated_y, title,
                                 description)

                plot.show() if self.show else plot.savefig(f"charts/{interpolation_method}/{file}-{smpl}-samples.png")

                self.index += 1

    @staticmethod
    def plot(org_x, org_y, probes_x, probes_y, interpolated_x, interpolated_y, title, description):
        plt.figure(figsize=(15, 9))
        plt.plot(org_x, org_y, label="Oryginalny wykres")
        plt.plot(probes_x, probes_y, 'o', markersize=12, label="Próbki", color="lime")
        plt.plot(interpolated_x, interpolated_y, label="Funkcja interpolacyjna")
        plt.title(title, fontsize=25)
        plt.legend(prop={'size': 16})
        plt.figtext(0.5, 0.001, description, wrap=True, horizontalalignment='center', fontsize=18)
        return plt

    def get_plot_title_and_description(self, method_name, file, smpl):
        filename = re.sub(r"(\w)([A-Z])", r"\1 \2", file)
        title = f"{method_name} dla {filename}, ilość próbek = {smpl}"
        description = f"wyk. {self.index} prezentuje przeprowadzenie interpolacji metodą Lagrange'a\n dla {smpl}" \
                      f" próbek z pliku {file}.csv "
        return description, title
