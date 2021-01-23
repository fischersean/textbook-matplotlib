import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

mpl.style.use("./style/textbook.mplstyle")


def main():
    # example data
    x = np.arange(0.1, 4, 0.5)
    y = np.exp(-x)

    # example variable error bar values
    yerr = 0.1 + 0.2 * np.sqrt(x)
    xerr = 0.1 + yerr

    fig, ax = plt.subplots()
    ax.errorbar(x, y, xerr=0.2, yerr=0.4, color="black")

    return fig, ax


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/errorbars.svg")
