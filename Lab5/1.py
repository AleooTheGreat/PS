import numpy as np
import matplotlib.pyplot as plt

train_file = np.genfromtxt("Train.csv", delimiter=',')
train_file = train_file[1:, 2]

# a
# Din moment ce sistemul inregistreaza odata pe ora, frecventa de esantionare este 1/1h = 1/3600s
fs = 1/3600
# b
# Avem 18288 de ore, deci 18288/24 = 762 de zile perioada de timp
print(f'Perioada de timp esantionata este {len(train_file)} ore = {len(train_file)/24} zile')

# c
# Frecventa maxima prezenta in semnal este 1/7200 pentru ca avem 1/3600 frecventa de esantionare si aplicand
# Nyquist care ne spune ca intr-un semnal X avem nevoie de cel putin 2 * frecventa maxima pentru a esantiona corect
# obtinem ca frecventa maxima = 1/2 * 1/3600 = 1/7200

# d
def d():
    train_fft = np.fft.fft(train_file)
    n = len(train_file)
    train_fft = np.abs(train_fft)

    f = fs * np.linspace(0,n//2,n//2)/n

    plt.figure(figsize=(24, 12))
    plt.plot(f, np.abs(train_fft[:n//2]) / n)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('FFT')
    plt.savefig('d.pdf')
    plt.grid(True)
    plt.show()

# e

mean_semnal = np.mean(train_file)
train_file -= mean_semnal
train_fft = np.fft.fft(train_file)
n = len(train_file)
train_fft = np.abs(train_fft)

f = fs * np.linspace(0,n//2,n//2)/n

plt.figure(figsize=(24, 12))
plt.plot(f, np.abs(train_fft[:n//2]) / n)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT')
plt.savefig('d.pdf')
plt.grid(True)
plt.show()


# t = np.linspace(0,1000, 1000)
# plt.figure(figsize=(24,12))
# plt.plot(t, train_file[:1000])
# plt.show()