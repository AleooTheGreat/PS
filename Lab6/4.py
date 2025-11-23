import numpy as np

pi = np.pi

def semnal_sinus(A,f,t,o):
    return A * np.sin(2 * pi * f * t + o)

t = np.linspace(0,1, 20)
d = 5
eps = 1e-10

x = semnal_sinus(1,5,t,0)
y = np.roll(x,d)

x_fft = np.fft.fft(x)
y_fft = np.fft.fft(y)

d2 = np.fft.ifft(np.matrix.conjugate(x_fft) * y_fft)

x_eps_fft = np.where(np.abs(x_fft) < eps, eps, x_fft)
d3 = np.fft.ifft(y_fft / x_eps_fft)


print(f'Initial d = {d}, iar dupa primul algoritm (cel cu inmultire) obtinem d = {np.argmax(np.abs(d2))}.')
print(f'Initial d = {d}, iar dupa al 2-lea algoritm (cel cu impartire + inlocuirea lui 0 cu o valoare foarte mica ca sa aiba sens impartirea) obtinem d = {np.argmax(np.abs(d3))}.')
