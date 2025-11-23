import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sc

# a

data = np.genfromtxt('Train.csv', delimiter=',', skip_header= 10000 + 1, max_rows= 72)
x = data[:,-1]
t = np.arange(72)
# b

w_values = [5,9,13,17]

fig, axs = plt.subplots(2,2, figsize = (24,16))
fig.suptitle('Normalizare de tip medie alunecatoare')
for i in range(len(w_values)):

    w = w_values[i]

    filtru = np.convolve(x, np.ones(w), 'valid') / w

    axs[i // 2, i % 2].set(xlabel = 'Timp (ore)', ylabel = 'Trafic', title = f'Semnal mediatizat cu w = {w}')
    axs[i // 2, i % 2].plot(t[:len(filtru)],filtru, color = 'black',label = f'Semnal normalizat cu w = {w}')
    axs[i // 2, i % 2].plot(t,x, '--', c = 'lightblue', label = 'Semnal original')
    axs[i // 2, i % 2].legend()
    axs[i // 2, i % 2].grid(True)

fig.savefig('6_b.pdf')
plt.show()

# c
# Frecventa noastra de esantionare fs = 1hz/ora, asa ca frecventa Nyquist este fs/2 = 1/2 hz/ora
# Alegem sa taiem tot ce este mai mic decat frecventa zilnica de fz = 1/24, deoarece traficul are
# periodicitate zilnica, deci Wn = fz/(fs/2) in [0,1]. Vom folosi filtrele Butterworth vs Chebyshev
# de ordin 5 (precum in curs, y[n] se calculeaza pe baza a x[n] x[n-5] si y[n-1] ..y[n-5])
# iar la Chebyshev am ales rp = 2.5 db deoare in documentatie se spune ca 5 este o valoare normala,
# dar ma gandesc ca daca prindem o perioada mai putin circulata 2.5 ar putea fi un compromis.

fs = 1/1
fn = 1/2 * fs
Wn = (1/24)/fn

b, a = sc.butter(5, Wn, btype='low')
x_butter_filtered = sc.filtfilt(b,a,x)

b, a = sc.cheby1(5, 2.5, Wn, btype='low')
x_cheby_filtered = sc.filtfilt(b, a, x)

plt.figure(figsize=(16, 12))

plt.plot(t, x, '--', color='lightblue', label='Semnal original')
plt.plot(t, x_butter_filtered, color='green', label='Butterworth (ord = 5)')
plt.plot(t, x_cheby_filtered, color='red', label='Chebyshev (ord = 5, rp = 2.5 dB)')

plt.xlabel('Timp (ore)')
plt.ylabel('Trafic')
plt.title('Butterworth vs Chebyshev')

plt.legend()
plt.grid(True)

plt.savefig('6_c.pdf')
plt.show()

# d

rp_values = [0.5, 1, 5, 10]

b, a = sc.butter(5, Wn, btype='low')
x_butter_filtered = sc.filtfilt(b,a,x)

fig, axs = plt.subplots(2,2, figsize = (24,16))
fig.suptitle('Butterworth vs Chebyshev')

for i in range(len(rp_values)):
    rp = rp_values[i]
    b, a = sc.cheby1(5, rp, Wn, btype='low')
    x_cheby_filtered = sc.filtfilt(b, a, x)

    axs[i // 2][i % 2].plot(t, x, '--', color='lightblue', label='Semnal original')
    axs[i // 2][i % 2].plot(t, x_butter_filtered, color='green', label='Butterworth (ord=5)')
    axs[i // 2][i % 2].plot(t, x_cheby_filtered, color='red', label=f'Chebyshev (ord=5, rp = {rp} dB)')

    axs[i // 2][i % 2].set(xlabel = ('Timp (ore)'), ylabel = ('Trafic'), title = (f'Butterworth vs Chebyshev_rp = {rp} dB'))
    axs[i // 2][i % 2].legend()
    axs[i // 2][i % 2].grid(True)

plt.savefig('6_d_e.pdf')
plt.show()

# e
# Aleg filtrul Butterworth pentru cazul nostru, deoarece are o banda de trecere plata
# si pastreaza forma si amplitudinea semnalului de trafic cat mai aproape de valorile reale.
# Deci varfurile de trafic si perioadele mai linistite sunt vizibile fara sa fie deformate puternic.
#
# Filtrul Chebyshev in special pentru valori mari ale lui rp, introduce ondulatii
# semnificative in banda de trecere si poate deforma prea mult anumite
# perioade facand sa para ca toate zilele sunt mai aglomerate sau mai line decat
# in realitate.

# f

ordin_values = [2,4,6,10]

for o in ordin_values:

    rp_values = [0.5, 1, 5, 10]

    b, a = sc.butter(o, Wn, btype='low')
    x_butter_filtered = sc.filtfilt(b,a,x)

    fig, axs = plt.subplots(2,2, figsize = (24,16))
    fig.suptitle('Butterworth vs Chebyshev')

    for i in range(len(rp_values)):
        rp = rp_values[i]
        b, a = sc.cheby1(o, rp, Wn, btype='low')
        x_cheby_filtered = sc.filtfilt(b, a, x)

        axs[i // 2][i % 2].plot(t, x, '--', color='lightblue', label='Semnal original')
        axs[i // 2][i % 2].plot(t, x_butter_filtered, color='green', label=f'Butterworth (ord={o})')
        axs[i // 2][i % 2].plot(t, x_cheby_filtered, color='red', label=f'Chebyshev (ord={o}, rp = {rp} dB)')

        axs[i // 2][i % 2].set(xlabel = ('Timp (ore)'), ylabel = ('Trafic'), title = (f'Butterworth ord = {o} vs Chebyshev ord = {o}, rp = {rp} dB'))
        axs[i // 2][i % 2].legend()
        axs[i // 2][i % 2].grid(True)

    plt.savefig(f'6_f_Ordin={o}.pdf')
    plt.show()