import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.style.use("./style/textbook.mplstyle")


def main():
    fig, ax = plt.subplots()
    ax.bar(
        [1, 2, 3],
        [1, 2, 3],
        tick_label=["a", "b", "c"],
        color="none",
        hatch="//",
    )

    return fig, ax


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/bar.svg")
