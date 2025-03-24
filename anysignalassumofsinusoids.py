import numpy as np
import matplotlib.pyplot as plt

sampling_rate=1000
duration=1

#define frequencies and amplitudes of the signals
frequencies=[5,50,100]
amplitudes=[1,0.5,0.4]

#define a time array to caculate signal values

t=np.linspace(0,duration,int(sampling_rate*duration))

#cretaing the signal value array
signal=np.zeros_like(t)
for f,A in zip(frequencies,amplitudes):
    signal+=A*np.sin(2*np.pi*f*t)

plt.figure(figsize=(10,6))
plt.plot(t, signal, label="combined signal")
plt.grid(True)
plt.show()    