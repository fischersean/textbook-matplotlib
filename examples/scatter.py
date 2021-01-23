import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use("./style/textbook.mplstyle")


def main():
    np.random.seed(2)

    fig, ax1 = plt.subplots()

    offset = 0.1
    x = np.arange(0.5, 15) + offset
    y = np.random.rand(15) + offset
    y2 = np.random.rand(15)

    ax1.scatter(
        x, y, label="a", marker="o", facecolor="none", edgecolor="black"
    )
    ax1.scatter(x, y2, label="b", marker="o", facecolor="black")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_xlim(0)
    ax1.set_ylim(0)

    return fig, ax1


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/scatter.svg")
