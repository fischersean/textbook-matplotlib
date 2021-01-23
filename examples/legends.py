import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use("./style/textbook.mplstyle")


def main():

    fig, ax = plt.subplots()
    np.random.seed(2)
    n = 25
    x = range(n)
    y = np.cumsum(np.random.randn(n))
    # unpack the single line2d artist
    (ln,) = ax.plot(
        x, y, color="black", marker="s", linestyle="-", label="plot"
    )
    ax.fill_between(x, y, 0, label="fill", hatch="//", facecolor="none")
    ax.scatter(
        n * np.random.rand(n),
        np.random.rand(n),
        label="scatter",
        color="black",
    )
    ax.set_ylim(-7, 2)
    ax.legend()

    return fig, ax


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/legends.svg")
