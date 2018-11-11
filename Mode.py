
import numpy as np

from Sinus import Sinus

class Mode:

    # input arguments are lists of parameters for Siuns objects
    def __init__(self, frequencies, kvects, amps):
        self.numberOfCurves = len(frequencies)
        self.sinuses = []

        for f, k, a in zip(frequencies, kvects, amps):
            # f unit is [1/s] nad k unit is [rad/m]
            self.sinuses.append(Sinus(f, k, (f/k) * 2*np.pi, a))

    def propagate(self, time, barLength, gainFactor):
        for s in self.sinuses:
            s.propagate(time, barLength, gainFactor)