import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def semnal_sinusoidal(A, t, f, omega):
    return A * np.sin( 2 * pi* t* f + omega)

def semnal_sawtooth(t,f):
    return 2 * (t * f - np.floor( 0.5 + t * f))

fig, axs = plt.subplots(3)
fig.suptitle('Sinus si Sawtooth')

t = np.linspace(0,0.1,200)
sin = semnal_sinusoidal(1,t,200,0)
saw = semnal_sawtooth(t,100)
suma = sin + saw

axs[0].plot(t,sin)
axs[0].grid(True)
axs[0].set_ylabel('Sin')


axs[1].plot(t,saw)
axs[1].grid(True)
axs[1].set_ylabel('Sawtooth')

axs[2].plot(t,suma)
axs[2].grid(True)
axs[2].set_ylabel('Sin + Sawtooth')

fig.supxlabel('Time')
fig.tight_layout()
plt.savefig('4.pdf')
plt.show()