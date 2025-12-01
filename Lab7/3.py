from scipy import datasets, ndimage
import numpy as np
import matplotlib.pyplot as plt

x = datasets.face(gray=True)
pixel_noise = 200

noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=x.shape)
X_noisy = x + noise

p_signal = np.sum(X_noisy**2)
p_noise = np.sum(noise ** 2)

snr_before = 10 * np.log10(p_signal / p_noise)

better_x = ndimage.gaussian_filter(X_noisy, sigma = 0.1)
better_x = np.where(better_x < 1e-13, 1e-13, better_x)

new_noise = X_noisy - better_x
snr_after = 10 * np.log10((np.sum(better_x**2))/ np.sum(new_noise ** 2))

fig, axs = plt.subplots(1,2, figsize = (12,10))
fig.suptitle('Imagine cu zgomot redus')

axs[0].imshow(X_noisy, cmap= plt.cm.gray)
axs[0].set(title = f'Imagine originala SNR = {round(snr_before,2)} dB')

axs[1].imshow(better_x, cmap = plt.cm.gray)
axs[1].set(title = f'Imagine cu zgomot redus SNR = {round(snr_after,2)} dB')

plt.tight_layout()
plt.savefig('3.pdf')
plt.show()