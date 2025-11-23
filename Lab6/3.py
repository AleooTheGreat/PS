import matplotlib.pyplot as plt
import numpy as np

p = np.random.randint(1,10, size = 5)
q = np.random.randint(1,10, size = 6)

n = len(p) + len(q) - 1
n = 2 ** int(np.ceil(np.log2(n)))

r = np.zeros(n)
# inmultirea polinoamelor directa

for i in range(len(p)):
    for j in range(len(q)):
        r[i+j] += p[i] * q[j]


# FFT
p = np.pad(p, (0, n - len(p)))
q = np.pad(q, (0, n - len(q)))

p_fft = np.fft.fft(p)
q_fft = np.fft.fft(q)

r_fft = p_fft * q_fft
r_ifft = np.fft.ifft(r_fft)


print(f' Coeficientii lui P = {p}')
print(f' Coeficientii lui Q = {q}')
print(f' Coeficientii lui R = P*Q = {r}')
print(f' Coeficientii lui R = IFFT(FFT(P)*FFT(Q)) = {np.round(r_ifft.real, 2)}')


