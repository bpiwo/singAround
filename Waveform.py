import numpy as np
from matplotlib import  pyplot as plt

from Mode import Mode
from CurvesSampling import findKvForGivenListOfFrequenciesInMode

class Waveform:

    def __init__(self, omegaPath, kvectPath, samplingFrequencies, numOfCurves, amplitude=1.0):
        self.modes = []

        frequencies = ( np.load(omegaPath) / (np.pi * 2) ).real
        kvect = np.load(kvectPath) * 1000

        # initializing amplitude array with the same shape as kvect
        amp = np.full((np.shape(samplingFrequencies)[0], 1), amplitude)

        for i in range(numOfCurves):
            samplingKvect = findKvForGivenListOfFrequenciesInMode(frequencies[i], kvect, samplingFrequencies)
            mode = Mode(samplingFrequencies, samplingKvect, amp)
            self.modes.append(mode)


    def propagate(self, time, barLength, gainFactor):
        for m in self.modes:
            m.propagate(time, barLength, gainFactor)

    def draw(self):
        freqAmplitude = []
        frequency = []

        for ind, m in enumerate(self.modes):
            for sind, s in enumerate(m.sinuses):
                if(ind == 0):
                    freqAmplitude.append(s.amplitude)
                    frequency.append(s.frequency)
                else:
                    freqAmplitude[sind] += s.amplitude

        plt.figure(1)
        plt.plot(frequency, freqAmplitude)
        plt.ylabel("Amplitude")
        plt.xlabel("Frequency")
        plt.xlim(5000, 1e5)
        plt.show()