import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
plt.rcParams['agg.path.chunksize'] = 10000
# import math

def getWav(filename):
    rate, data = wavfile.read(filename)
    data = data/(32768.)
    data = np.float32(data)
    # plt.plot(range(0, len(data)), data)
    # plt.grid()
    # plt.show()
    # input()
    return rate, data

def flang(filename):
    rate, data = getWav(filename)

    b = []
    b.append(1)
    m_n1 = 2 * np.pi * 13/44100
    m_n2 = m_n1 * float(len(data))
    m_n3 = np.sin(m_n2)
    m_n4 = 0.0128 * rate * m_n3
    m_n5 = 1 + m_n4
    m_n6 = int(m_n5)
    for i in range(m_n6):
        b.append(0)
    b.append(0)
    a = [1]
    y = signal.lfilter(b, a, data)
    y = np.float32(y)
    # plt.plot(range(0, len(y)), y)
    # plt.grid()
    # plt.show()
    # input()
    wavfile.write(filename+'FLANG.wav', rate, y)
    # y[n] = (1-0.25)x[n-100] + (0.25)x[n-101]

flang('guitar.wav')
