import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use("./style/textbook.mplstyle")


def main():
    data = np.random.lognormal(size=(37, 4))
    fig, ax = plt.subplots()
    ax.boxplot(data, labels=["A", "B", "C", "D"])
    ax.set_yscale("log")

    return fig, ax


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/boxplot.svg")
