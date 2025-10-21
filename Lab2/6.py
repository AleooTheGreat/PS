import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,0.1, 200)
pi = np.pi
fs = 100
def semnal_sinus(A, f, t, omega):
    return A * np.sin(2 * pi * t * f + omega)

fig, axs = plt.subplots(3)
fig.suptitle(f' {fs/2}, {fs/4}, 0 hz')

axs[0].plot(t, semnal_sinus(1,fs/2,t,0))
axs[0].grid(True)
axs[0].set_ylabel(f'{fs/2} hz')

axs[1].plot(t, semnal_sinus(1,fs/4,t,0))
axs[1].grid(True)
axs[1].set_ylabel(f'{fs/4} hz')

axs[2].plot(t, semnal_sinus(1,0,t,0))
axs[2].grid(True)
axs[2].set_ylabel('0 hz')

fig.supxlabel('Time')
fig.tight_layout()
plt.savefig('6.pdf')
plt.show()