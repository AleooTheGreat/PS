import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def x(t):
    return np.cos(520*np.pi*t + np.pi/3)

def y(t):
    return np.cos(280*np.pi*t - np.pi/3)

def z(t):
    return np.cos(120*np.pi*t + np.pi/3)

# a

t = np.linspace(0.0,0.03, int(0.03/0.0005))
print(t)

# b

fig, axs = plt.subplots(3)
fig.suptitle('Semnale x(t), y(t), z(t)')

axs[0].plot(t,x(t))
axs[0].grid(True)
axs[0].set_ylabel('x(t)')

axs[1].plot(t,y(t))
axs[1].grid(True)
axs[1].set_ylabel('y(t)')

axs[2].plot(t,z(t))
axs[2].grid(True)
axs[2].set_ylabel('z(t)')

fig.supxlabel('time')
plt.savefig('1a.pdf')
fig.show()


# c

t = np.linspace(0,0.03,int(0.03 * 200))
print(t)
fig, axs = plt.subplots(3)
fig.suptitle('Semnale x(t), y(t), z(t)')

axs[0].stem(t,x(t))
axs[0].grid(True)
axs[0].set_ylabel('x(t)')

axs[1].stem(t,y(t))
axs[1].grid(True)
axs[1].set_ylabel('y(t)')

axs[2].stem(t,z(t))
axs[2].grid(True)
axs[2].set_ylabel('z(t)')

fig.supxlabel('time')
plt.savefig('1b.pdf')
fig.show()
