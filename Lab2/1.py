import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def semnal_sin(A, f, t, omega):
    return A * np.sin( 2 * pi * f * t + omega)

def semnal_cos(A, f, t, omega):
    return A * np.cos( 2 * pi * f * t + omega)

t = np.linspace(0,0.1,200)

fig, axs = plt.subplots(2)
fig.suptitle('Semnal Sinusoidal si Cosinusoidal')

axs[0].plot(t,semnal_sin(3,400,t,0))
axs[0].grid(True)
axs[0].set_ylabel('Sinus')

axs[1].plot(t,semnal_cos(3,400,t,-pi/2))
axs[1].grid(True)
axs[1].set_ylabel('Cosinus')

fig.supxlabel('Time')
plt.savefig('1.pdf')
fig.show()