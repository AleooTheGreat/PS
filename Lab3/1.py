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


fig, axs = plt.subplots(n,figsize = (10,14))
fig.suptitle("Matricea Fourier - Componente Reale si Imaginare")

for i in range(n):
    axs[i].set(ylim = (-1.1,1.1), title = f'Randul {i}')

    axs[i].plot(m[i, :].real, color = 'red', label = 'Partea Reala')
    axs[i].grid(True)

    axs[i].plot(m[i, :].imag,'--', color = 'green', label = 'Partea Imaginara')
    axs[i].grid(True)

plt.legend()
plt.savefig("1.pdf")
plt.tight_layout()
plt.show()