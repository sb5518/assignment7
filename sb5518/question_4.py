__author__ = 'sb5518'
import warnings
import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt

"""This class corresponds to question 4. It pop's up a Mandelbrot Fractal"""

warnings.simplefilter("ignore")

class question_4:
    @staticmethod
    def question4(): #This function prints the answer to question 4 when called
        N_max = 50
        some_threshold = 50

        x = np.array(np.linspace(-2, 1, 400), dtype=np.float128)
        y = np.array(np.linspace(-1.5, 1.5, 400), dtype=np.float128)

        c = x[:, newaxis] + 1j*y[newaxis, :]
        z = c

        for g in range(some_threshold):
                z = z**2 + c

        threshold = N_max
        mask = np.abs(z) < threshold

        plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
        plt.gray()
        plt.savefig("mandelbrot.png")

