from contextlib import redirect_stdout
import numpy as np

import matplotlib.pyplot as plt

class VQELog:
    """Capture output from a VQE run. This a thin wrapper around redirect_stdout
    """

    def __init__(self):
        self.parameter_set = None
        self.evals = []
        self.means = []
        self.stds = []

    def append(self, eval_count, parameter_set, mean, std):
        """Callback function
        """
        self.evals.append(eval_count)
        self.means.append(mean)
        self.stds.append(std)

    def plot(self):
        fig, ax = plt.subplots(1,1)

        # make things numpy arrays so we can do vector arithmetic transparently
        evals = np.array(self.evals)
        means = np.array(self.means)
        stds = np.array(self.stds)

        ax.plot(evals, means)
        ax.fill_between(evals, means - stds, means + stds, alpha=0.5)
        ax.set_xlabel('Evaluations')
        ax.set_ylabel('Energy')
        ax.set_title('VQE convergence')
        plt.tight_layout()

        return fig
