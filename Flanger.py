import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from decimal import Decimal
# plt.rcParams['agg.path.chunksize'] = 10000
# import math
# M(o) = 13Hz
# A = 12.8 ms
# b = g + z-1
# a = 1 + gz-1
# g = 1-x / 1 + x


def getWav(filename):
    rate, data = wavfile.read('source_wav/'+filename)
    data = data/(32768.)
    data = np.float32(data)
    # plt.plot(range(0, len(data)), data)
    # plt.grid()
    # plt.show()
    # input()
    return rate, data

def flang(filename, f_rate, depth, new_filename):
    samp_rate, data = getWav(filename)
    nsamp = len(data)
    Mo = 0.013 * samp_rate
    excursion = 1
    b = []
    b.append(1)
    m_n1 = 2 * np.pi * f_rate/samp_rate
    m_n2 = m_n1 * nsamp
    m_n3 = np.sin(m_n2)
    m_n4 = excursion * m_n3
    m_n5 = 1 + m_n4
    m_n6 = Mo * m_n5
    if(not m_n6.is_integer()):
        g_d = float(Decimal(str(m_n6)) % 1)
        g_ = (1 - g_d) / (1 + g_d)
        b_ = [g_, 1]
        a_ = [1, g_]
        M_ = m_n6 - g_d
        b = []
        b.append(1)
        for i in range(int(M_)):
            b.append(0)
        b.append(depth)
        a = [1]
        data_1 = signal.lfilter(b, a, data)
        data_2 = signal.lfilter(b_, a_, data_1)
        final_data = data_2
    else:
        b.append(1)
        for i in range(int(M_)):
            b.append(0)
        b.append(depth)
        a = [1]
        data_1 = signal.lfilter(b, a, data)
        final_data = data_1
    orig_filename = 'abcdc.com'
    if filename.endswith('.wav'):
        filename = filename[:-4]
    wavfile.write(new_filename+'_FLANGED.wav', samp_rate, final_data)

# flang('guitar.wav', 20, 1)
