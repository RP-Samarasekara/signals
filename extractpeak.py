import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavefile
from scipy.fft import fft

def find_peak_frequency(signal,sample_rate):
    #number of samples of signal
    N=len(signal)

    #apply fft to conver signal in to frequency domain
    yf=fft(signal)
    xf=


#we define the sampling rate
sample_rate=44000
sample_rate,signal= wavefile.read('sample.wav') 

if len(signal.shape)==2:
    signal=signal.mean(axis=1)


    