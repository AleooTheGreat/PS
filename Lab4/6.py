import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wv
from sympy.physics.vector import vprint

freq, vocale = wv.read('vocale.wav')

vocale = vocale[:,0]
n = len(vocale)
window_size = int(0.01 * n)
step = int(window_size * 0.5)

windows = []

for i in range(0, n - window_size, step):
    val = vocale[i:i+window_size]
    val_fft = np.abs(np.fft.rfft(val))
    windows.append(val_fft)

spect = np.column_stack(windows)

# Pregatim un array cu frecventele in Hz de la 0 pana la Nyquist, normalizat
frq = np.fft.rfftfreq(window_size, d=1.0 / freq)

# Numarul de ferestre * (durata in secunde (step/freq))
times = np.arange(spect.shape[1]) * (step / float(freq))

spect_db = 10 * np.log10(spect)


plt.figure(figsize=(12, 10))
plt.pcolormesh(times, frq, spect_db, cmap='magma')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Spectrogram')
plt.colorbar(label='Amplitude')
plt.savefig('6.pdf')
plt.tight_layout()
plt.show()