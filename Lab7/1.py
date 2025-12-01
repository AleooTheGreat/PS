import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

pi = np.pi

n = np.linspace(0,1,200)
x = np.zeros((len(n),len(n)))

def refresh(x_ref):
    x_ref = np.zeros((len(n), len(n)))
    return x_ref

def a(x):
    for i in range(len(n)):
        for i2 in range(len(n)):
            x[i,i2] = np.sin(2 * pi * n[i] + 3 * pi * n[i2])

    return x, "sin(2*pi*n1 + 3*pi*n2)", 'a'

def b(x):
    for i in range(len(n)):
        for i2 in range(len(n)):
            x[i, i2] = np.sin(4 * pi * n[i]) + np.cos(6 * pi * n[i2])

    return x, "sin(4*pi*n1) + cos(6*pi*n2)", 'b'

def c(Y):
    Y[0, 5] = 1
    Y[0, len(n) - 5 ] = 1

    return Y, "Y[0,5] = Y[0,n-5] = 1", 'c'

def d(Y):
    Y[5, 0] = 1
    Y[len(n) - 5, 0] = 1

    return Y, "Y[5,0] = Y[n-5,0] = 1", 'd'

def e(Y):
    Y[5, 5] = 1
    Y[len(n) - 5, len(n) - 5 ] = 1

    return Y, "Y[5,5] = Y[n-5,n-5] = 1", 'e'

def plot(x, st, s):
    fig, axs = plt.subplots(1,2,figsize = (12,10))
    fig.suptitle(st)

    axs[0].imshow(x, cmap=plt.cm.gray)
    axs[0].set(title = 'Imagea originala')

    x_fft = 20 * np.log10(np.maximum(abs(np.fft.fft2(x)), 1e-13))
    axs[1].imshow(x_fft)
    axs[1].set(title = 'Spectru')

    plt.tight_layout()
    fig.colorbar(axs[1].images[0], ax=axs[1])
    plt.savefig(f'1_{s}.pdf')
    plt.show()

def plot2(Y, st, s):
    fig, axs = plt.subplots(1,2,figsize = (12,10))
    fig.suptitle(st)

    axs[0].imshow(np.real(np.fft.ifft2(Y)), cmap=plt.cm.gray)
    axs[0].set(title = 'Imagea originala')

    axs[1].imshow(20 * np.log10(np.maximum(abs(Y), 1e-13)))
    axs[1].set(title = 'Spectru')

    plt.tight_layout()
    fig.colorbar(axs[1].images[0], ax=axs[1])
    plt.savefig(f'1_{s}.pdf')
    plt.show()

plot(*a(x))
x = refresh(x)

plot(*b(x))
x = refresh(x)

plot2(*c(x))
x = refresh(x)

plot2(*d(x))
x = refresh(x)

plot2(*e(x))
