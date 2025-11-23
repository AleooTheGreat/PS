import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

def fereastra_drept(n):
    return np.ones(n)

def fereastra_hanning(n):
    t = np.arange(n)
    return 0.5 * (1 - np.cos((2 * pi * t) / (n-1)))

t = np.linspace(0, 1, 200)
x = 1 * np.sin( 2 * pi * 100 * t + 0)

w_drept = x * fereastra_drept(200)
w_hanning = x * fereastra_hanning(200)

fig, axs = plt.subplots(2,2,figsize = (24,20))
fig.suptitle('Fereasta Dreptunghi vs Hanning')

axs[0, 0].plot(t, w_drept, color='red', label='Fereastra dreptunghi')
axs[0, 0].set(xlabel='Timp [s]', ylabel='Amplitudine', title='Semnal cu fereastra dreptunghiulara')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(t, w_drept, color='red', label='Fereastra dreptunghi')
axs[0, 1].plot(t, x, '--', color='lightgray', label='Semnal original', alpha=0.7)
axs[0, 1].set(xlabel='Timp [s]', ylabel='Amplitudine', title='Dreptunghi vs Original')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(t, w_hanning, color='green', label='Fereastra Hanning')
axs[1, 0].set(xlabel='Timp [s]', ylabel='Amplitudine', title='Semnal cu fereastra Hanning')
axs[1, 0].legend()
axs[1, 0].grid(True)

axs[1, 1].plot(t, w_hanning, color='green', label='Fereastra Hanning')
axs[1, 1].plot(t, x, '--', color='lightgray', label='Semnal original', alpha=0.7)
axs[1, 1].set(xlabel='Timp [s]', ylabel='Amplitudine', title='Hanning vs Original')
axs[1, 1].legend()
axs[1, 1].grid(True)


plt.tight_layout()
plt.savefig('5.pdf')
plt.show()
