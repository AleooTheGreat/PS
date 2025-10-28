import numpy as np
import matplotlib.pyplot as plt
import math

e = math.e
pi = math.pi
n = 8

def fourier_mat(n):
    mat = np.ones([n,n], dtype=complex)
    for i in range(1,n):
        for j in range(1,n):
            w = e**(-2*pi*1j*i*j/n)
            mat[i][j] = w
    return mat

m = fourier_mat(n)

trans = np.conj(m.T)
prod = m @ trans
print(np.allclose(prod, prod[0][0] * np.eye(n)))


fig, axs = plt.subplots(8,2)
fig.suptitle("Matricea Fourier")

for i in range(n):
    axs[i, 0].plot(m[i, :].real)
    axs[i, 0].grid(True)

    axs[i, 1].plot(m[i, :].imag)
    axs[i, 1].grid(True)

plt.show()