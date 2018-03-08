import matplotlib.pyplot as plt
import numpy
from scipy.io.wavfile import read,write
import random

msg = "Hello world"
bits = str(bin(int.from_bytes(msg.encode(), 'big')))[2:]
N_bits = len(bits)
#MAP 0->-1,1->1
#Format 0bXXXXXX it's why we sky the first 2 element
symbols = list(map(lambda x: 2*int(x)-1,bits))

Fs = 44100
R = 100
N_samples = round(Fs/R)
SNR_dB = -20

spread_waveform = [2*round(random.random())-1 for x in range(N_samples)]
modulated_signal = []
for i in range(N_bits):
    sample = map(lambda x: x*symbols[i],spread_waveform)
    modulated_signal.append(list(sample))


"""
plt.plot(modulated_signal)
plt.ylabel('Modulated Signal')
plt.show()
"""

a = read("test.wav")
music = numpy.array(a[1],dtype=float)
modulated_signal = numpy.array(modulated_signal)
modulated_signal.resize(music.shape)
watermarked_signal = modulated_signal + music
write("watermarked_signal.wav",44100,watermarked_signal)

plt.plot(modulated_signal[:300])
plt.plot(watermarked_signal[:300])
plt.show()
