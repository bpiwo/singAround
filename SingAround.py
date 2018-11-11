import numpy as np

from Waveform import Waveform




if __name__ == '__main__':
    omegaPath = 'omega.npy'
    kvectPath = 'kvect.npy'
    samplingFrequencies = np.linspace(5e3, 1e5, 200)
    numOfCurves = 3

    wave = Waveform(omegaPath, kvectPath, samplingFrequencies, numOfCurves)
    for i in range(100):
        wave.propagate(0.1, 2.1, gainFactor=1.05)
        wave.draw()