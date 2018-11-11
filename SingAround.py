import numpy as np

from Waveform import Waveform


if __name__ == '__main__':
    omegaPath = 'omega.npy'
    kvectPath = 'kvect.npy'
    samplingFrequencies = np.linspace(5e3, 1e5, 200)
    numOfCurves = 4
    timeOfPropagation = 0.1
    lengthOfBar = 10.1
    gain = 1.05
    numberOfIterations = 100

    # creating waveform
    wave = Waveform(omegaPath, kvectPath, samplingFrequencies, numOfCurves)

    # propagation
    for i in range(numberOfIterations):
        wave.propagate(timeOfPropagation, lengthOfBar, gainFactor=gain)
        wave.draw()