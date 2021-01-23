import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
plt.style.use("textbook")

# Fixing random state for reproducibility
np.random.seed(19680801)

def main():
    N_points = 100000
    n_bins = 20

    # Generate a normal distribution, center at x=0 and y=5
    x = np.random.randn(N_points)
    y = .4 * x + np.random.randn(100000) + 5

    fig, ax = plt.subplots()

    # We can set the number of bins with the `bins` kwarg
    ax.hist(x, bins=np.arange(-6, 6, 0.5), color='lightgrey')

    return fig, ax


if __name__ == "__main__":
    fig, _ = main()
    fig.savefig("examples/exports/hist.svg")
