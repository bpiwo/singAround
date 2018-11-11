import numpy as np

def findKvForGivenListOfFrequenciesInMode(frequencies, kvect, givenFreqList):
    kv = [] # list to store kvect in sampling frequencies
    for f in givenFreqList:
        kv.append(findKvForGivenFreqInMode(frequencies, kvect, f))

    return kv

def findKvForGivenFreqInMode(frequencies, kvects, givenFreq):
    for i in range(len(frequencies) - 1):

        if(givenFreq < frequencies[0]):
            return kvects[0]

        if(givenFreq > frequencies[i] and givenFreq < frequencies[i+1]):

            # if frequency is between two points of curve calculate sample
            return valueBetweenPoints(givenFreq, frequencies[i], frequencies[i+1], kvects[i], kvects[i+1])

    return kvects[-1] # if frequency is bigger than the biggest from curve return last element of kvect

def valueBetweenPoints(argument, arg1, arg2, value1, value2):
    a = (value1 - value2) / (arg1 - arg2)
    b = value1 - arg1 * a

    return a * argument + b  # point of linear fc
