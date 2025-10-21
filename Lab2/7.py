import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,0.01, 200)
pi = np.pi

def semnal_sinus(A, f, t, omega):
    return A * np.sin(2 * pi * t * f + omega)

fig, axs = plt.subplots(2)
fig.suptitle('Semnal 1000hz si 1/4 din frecventa initiala')
fig.supxlabel('Timp')

#a
axs[0].plot(t,semnal_sinus(1,1000,t,0))
axs[0].grid(True)
axs[0].set_ylabel('Sinus 1000 hz')

t2 = t[::4]
semnal_decimizat = semnal_sinus(1,1000,t,0)[::4]

axs[1].plot(t2,semnal_decimizat)
axs[1].grid(True)
axs[1].set_ylabel('1/4 decimizare')

fig.tight_layout()
plt.savefig('7a.pdf')
plt.show()

#b
fig2, axs2 = plt.subplots(2)
fig2.suptitle('Semnal 1000hz si 1/4 din frecventa initiala de la al 2-lea element')
fig2.supxlabel('Timp')

axs2[0].plot(t,semnal_sinus(1,1000,t,0))
axs2[0].grid(True)
axs2[0].set_ylabel('Sinus 1000 hz')

t2_2 = t[1::4]
semnal_decimizat_2 = semnal_sinus(1,1000,t,0)[1::4]

axs2[1].plot(t2_2,semnal_decimizat_2)
axs2[1].grid(True)
axs2[1].set_ylabel('1/4 decimizare')

fig2.tight_layout()
plt.savefig('7b.pdf')
plt.show()