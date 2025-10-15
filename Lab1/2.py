import numpy as np
import matplotlib.pyplot as plt

def semnal_sinusoidal(t,f):
    return np.sin(2*np.pi*t*f)

def semnal_sawtooth(t,f):
    return 2 * (t * f - np.floor(1/2+t*f))

def semnal_square(t,f):
    return np.sign(np.sin(2 * np.pi * f * t))

def procedura_x(x,y):
    aux = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            if i == j or i == 0 or j == 0 or i == x - 1 or j == y - 1 or i+j == x:
                aux[i][j] = 1
    return aux


#a
t = np.linspace(0,0.1,1600)

plt.plot(t,semnal_sinusoidal(t,400))
plt.title('Semnal sinusoidal 400 hz, 1600 esantioane')
plt.xlabel('Timp')
plt.ylabel('Frecventa')
plt.savefig('2a.pdf')
plt.show()

#b

t = np.linspace(0,3,1600)

plt.plot(t,semnal_sinusoidal(t,800))
plt.title('Semnal sinusoidal 800 hz, 3 secunde')
plt.grid(True)
plt.xlabel('Timp')
plt.ylabel('Frecventa')
plt.savefig('2b.pdf')
plt.show()

#c

t = np.linspace(0,0.05,1600)

plt.plot(t,semnal_sawtooth(t,240))
plt.title('Semnal sawtooth 240 hz')
plt.grid(True)
plt.xlabel('Timp')
plt.ylabel('Frecventa')
plt.savefig('2c.pdf')
plt.show()

#d

t = np.linspace(0,0.03,1600)

plt.plot(t,semnal_square(t,300))
plt.title('Semnal square 300 hz')
plt.grid(True)
plt.xlabel('Timp')
plt.ylabel('Frecventa')
plt.savefig('2d.pdf')
plt.show()

#e

img = np.random.rand(128,128)

plt.title('Semnal 2D aleator')
plt.imshow(img)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('2e.pdf')
plt.show()

#f

img = procedura_x(128,128)

plt.title('Semnal X')
plt.imshow(img)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('2f.pdf')
plt.show()