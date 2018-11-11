import numpy as np

class Sinus:

    def __init__(self, freq, kv, vp, amp, length=0):
        self.frequency = freq
        self.kvect = kv
        self.vPhase = vp
        self.amplitude = amp
        self.propagatedLength = length
        self.totalPropagatedLength = length
        self.numOfGains = 0
        self.lastGainPhase = 0

    def propagate(self, time, barLength, gainFactor):
        self.propagatedLength += self.vPhase * time
        self.totalPropagatedLength += self.vPhase * time

        # gain amplitude for every time it goes all bar length
        while(self.propagatedLength - barLength > 0):
            self.propagatedLength -= barLength
            # calculate phase tha sinus has at the end of the bar
            gainPhase = self.lastGainPhase + self.kvect*barLength
            self.lastGainPhase = self.__reduceAngleInRadians(gainPhase)

            gainedAmplitude = self.amplitude * abs(np.sin(self.lastGainPhase))
            ungainedAmplitude = self.amplitude - gainedAmplitude

            self.amplitude = gainFactor * gainedAmplitude + ungainedAmplitude

        self.printSinusProperties()


    def __reduceAngleInRadians(self, angle):
        while(angle > np.pi * 2):
            angle -= np.pi*2

        return angle

    def printSinusProperties(self):
        print("Sinus, freq= ", self.frequency, ", kvect= ", self.kvect, ", vphase= ", self.vPhase,
              " amplitude= ", self.amplitude)