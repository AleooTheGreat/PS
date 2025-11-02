import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

pi = np.pi
e = np.e
n = 300

def fourier_mat(n):
    mat = np.ones([n,n], dtype=complex)
    for i in range(1,n):
        for j in range(1,n):
            w = e ** (-2 * pi * 1j * i * j/n)
            mat[i][j] = w
    return mat


def sinusoid(a,t,f,o):
    return a * np.sin(2 * pi * t * f + o)

t = np.linspace(0,1,300)
f1 = sinusoid(3,t,40,3)
f2 = sinusoid(4,t,80,0)
f3 = sinusoid(6,t,124,1)
f4 = sinusoid(1,t,234,5)
f5 = sinusoid(2,t,250,2)

f = f1 + f2 + f3 + f4 + f5

mat = fourier_mat(n)
x = mat @ f

fig, axs = plt.subplots(2,figsize = (20,10))
fig.suptitle('Semnal compus si Spectrul Fourier')

axs[0].plot(t,f)
axs[0].set(xlabel = 'Timp', ylabel = 'x(t)', title = 'Semnal compus')
axs[0].grid(True)

axs[1].stem(np.arange(0,300),np.abs(x[:300]))
axs[1].set(xlabel = 'Frecventa', ylabel = 'Amplitudine', title = 'Spectrul Fourier')
axs[1].grid(True)

plt.tight_layout()
plt.savefig('3.pdf')
plt.show()

