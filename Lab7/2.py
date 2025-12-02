from scipy import datasets
import numpy as np
import matplotlib.pyplot as plt

x = datasets.face(gray=True)

snr = 20

fig, axs = plt.subplots(1,2)
fig.suptitle(f'Matrice comprimata la {snr} db')

y = np.fft.fft2(x)

sgn_p = np.sum(np.abs(y) ** 2)
snr = 10 ** (snr/10)

p_noise = sgn_p/snr

Y_flat = np.abs(y).flatten()

sorted_i = np.argsort(Y_flat)

partial_sum = np.cumulative_sum(Y_flat[sorted_i] ** 2)
k = np.searchsorted(partial_sum,p_noise)
stop = Y_flat[sorted_i[k]]

mask = (Y_flat >= stop).reshape(y.shape)
Y_comp = y * mask
X_comp = np.real(np.fft.ifft2(Y_comp))

axs[0].imshow(x, cmap= plt.cm.gray)
axs[0].set(title = 'Imagine originala')

axs[1].imshow(X_comp, cmap = plt.cm.gray)
axs[1].set(title = 'Imagine comprimata')

plt.tight_layout()
plt.savefig('2.pdf')
plt.show()