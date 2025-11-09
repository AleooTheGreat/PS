import numpy as np
import matplotlib.pyplot as plt
import time
pi = np.pi
e = np.e

def semnal_sinus(a,f,t,o):
    return a * np.sin(2 * pi * f * t + o)

def dft(s, n):
    mat = np.ones([n,n], dtype=complex)
    for i in range(1,n):
        for j in range(1,n):
            w = e**(-2*pi*1j*i*j/n)
            mat[i][j] = w

    #mat = mat * (1/np.square(n))
    return mat @ s

def fft(s, n):
    if n <= 1:
        return s

    even = fft(s[::2], n//2)
    odd = fft(s[1::2], n//2)

    w = e ** (-2j * pi * np.arange(n//2)/n)
    t = w * odd

    return np.concatenate([even + t, even - t])

v_n = [128, 256, 512, 1024, 2048, 4096, 8192]
dft_times = []
fft_times = []
np_fft_times = []
for N in v_n:

    x = np.random.rand(N)

    time_dft = time.time()
    v_dft = dft(x, N)
    time_dft = time.time() - time_dft

    time_np_fft = time.time()
    v_np_fft = np.fft.fft(x)
    time_np_fft = time.time() - time_np_fft

    time_fft = time.time()
    v_fft = fft(x, N)
    time_fft = time.time() - time_fft

    dft_times.append(time_dft)
    fft_times.append(time_fft)
    np_fft_times.append(time_np_fft)

plt.figure(figsize=(12,15))


plt.plot(v_n, dft_times, 'o-', label = 'DFT')
plt.plot(v_n, fft_times, 'o-', label = 'FFT')
plt.plot(v_n, np_fft_times, 'o-', label = 'FFT optimizat (numpy)')
plt.yscale('log')
plt.xlabel("N (dimensiunea vectorului)")
plt.ylabel("Timp (log)")
plt.title("DFT vs FFT vs np.fft.fft")
plt.legend()
plt.grid(True)

plt.savefig('1.pdf')
plt.show()
