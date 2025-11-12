from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import torch
from IPython.core.pylabtools import figsize
from fontTools.misc.psCharStrings import t1Operators
from matplotlib.pyplot import xlabel, ylabel

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
def d(tf):
    train_fft = np.fft.fft(tf)
    n = len(tf)
    train_fft = np.abs(train_fft)

    f = fs * np.linspace(0,n//2,n//2)/n

    plt.figure(figsize=(24, 20))
    plt.plot(f, np.abs(train_fft[:n//2]) / n)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('FFT')
    plt.savefig('d.pdf')
    plt.grid(True)
    plt.show()

# e
# Am obervat ca media nu este zero deci avem un semnal cu offset asa ca vom scadea media pentru a elimina offsetul.
def e(tf):
    mean_semnal = np.mean(tf)
    tf_mean = tf.copy()
    tf_mean -= mean_semnal

    tf_fft = np.fft.fft(tf)
    tf_mean_fft = np.fft.fft(tf_mean)

    n = len(tf_fft)

    train_fft = np.abs(tf_fft)/n
    train_fft_mean = np.abs(tf_mean_fft)/n

    t = np.linspace(0,len(tf)//24, len(tf))
    f = fs * np.linspace(0,n//2,n//2)/n

    fig, axs = plt.subplots(2,2, figsize = (24,20))
    fig.suptitle('Original vs Normalizare')
    axs[0][0].plot(f, train_fft[:n//2])
    axs[0][0].set(xlabel = ('Frequency'), ylabel = ('Magnitude'), title = ('FFT original'))
    axs[0][0].grid(True)

    axs[0][1].plot(t, tf)
    axs[0][1].set(xlabel = ('Time(days)'), ylabel=('Number of Cars'), title=('FFT normalizat'))
    axs[0][1].grid(True)

    axs[1][0].plot(f, train_fft_mean[:n//2])
    axs[1][0].set(xlabel = ('Frequency'), ylabel = ('Magnitude'), title = ('Semnal original'))
    axs[1][0].grid(True)

    axs[1][1].plot(t, tf_mean)
    axs[1][1].set(xlabel = ('Time(days)'), ylabel=('Number of Cars'), title=('Semnal normalizat'))
    axs[1][1].grid(True)

    plt.savefig('e.pdf')
    plt.show()

def f(tf):
    tf_mean = tf.copy()
    tf_mean = tf_mean - np.mean(tf)

    tf_fft = np.fft.fft(tf)
    tf_fft_mean = np.fft.fft(tf_mean)

    n = len(tf_fft)

    tf_fft_mean = np.abs(tf_fft_mean[:n//2] / n)
    tf_fft = np.abs(tf_fft[:n//2] / n)

    i_mean = np.argsort(tf_fft_mean)
    i = np.argsort(tf_fft)

    i_mean = i_mean[::-1]
    i = i[::-1]

    print()
    print('Subpunctul f:')
    print(f'Primele 4 valori normalizate sunt: {i_mean[0]},{i_mean[1]},{i_mean[2]},{i_mean[3]}')
    print(f'Primele 4 valori nenormalizate sunt: {i[0]},{i[1]},{i[2]},{i[3]}')
    print('Obervam ca prima componenta este cea de medie daca nu normalizam, apoi avem 1,2 si 762 (18288/24), respectiv 3 in \n'
          'cazul normalizat. 1,2,3 apar pentru ca exista disproportinalitati destul de mari in anumite sezoane comparativ cu anii precedenti, \n'
          'iar 762 este echivalent cu 24 de ore, dar este normal ca in timpul saptamanii traficul sa fie mai mare decat in weekend, iar la \n'
          'pranz mai mare decat dimineata si noaptea.')

def g(tf):
    ## conform calendarului din 2013, 1 Aprilie a fost o zi de luni
    ## setul incepe din 25-08-2012
    d1 = date(2012,8,25)
    d2 = date(2013,4,1)

    padding = np.abs(d1-d2).days * 24
    luna = 24 * 7 * 7 # > 1000

    tf_luna = tf[padding: padding + luna]
    t = np.linspace(0,luna,luna)

    plt.figure(figsize=(24, 20))
    plt.plot(t, tf_luna)
    plt.xlabel('Timp(zile)')
    plt.ylabel('Numar de masini')
    plt.title('O luna de trafic (aproximativ 7 saptamani)')
    plt.savefig('g.pdf')
    plt.grid(True)
    plt.show()

def h():
    # As grupa traficul la nivel de luna si as cauta lunile cu cel mai mare trafic mediu sau total.
    # Presupun ca cea mai aglomerata luna sunt Decembrie, pentru ca atunci sunt sarbatorile de iarna,
    # dar selectez si 2 saptamani dupa aceasta din Ianuarie datorita Revelionului.
    # In perioada asta o sa fie mult trafic inainte de Craciun si Revelion, dar in zilele de Craciun
    # si Anul Nou o sa fie o scadere mare pentru ca oamenii deja au ajuns la destinatie.
    # Ultima zi cu trafic scazut din perioada asta o consider ziua de Anul Nou.
    # De acolo merg cam 3-5 luni inainte, adica spre primavara sau inceputul verii, unde traficul ar
    # trebui sa se stabilizeze si sa revina la normal. In zona asta selectez o perioada de o luna (31 de zile)
    # in care nu par sa fie evenimente.
    # Impart cele 31 de zile pe saptamani si ma uit la media traficului pe zile. In mod normal traficul ar
    # trebui sa fie mai mare in timpul saptamanii (luni pana vineri) si mai mic in weekend (sambata si duminica).
    # Caut saptamana unde se vede cel mai clar diferenta intre zilele de lucru si weekend, adica traficul
    # e mare 5 zile si apoi scade 2 zile. Ziua cu cel mai mic trafic din acea saptamana o consider
    # duminica, si din ea pot deduce celelalte zile. Iar in raport cu selectia de la Revelion
    # pana in ziua dedusa de duminica pot deduce fiecare zi din an.
    # Singura problema e ca pot exista exceptii (sarbatori, evenimente, vreme) si graficul saptamanii poate fi mai
    # mic in unele perioade, asa ca estimarea poate avea o eroare considerabila de cateva zile.
    pass

def i(tf):
    origin = tf.copy()

    tf_mean = tf.copy()
    tf_mean = tf_mean - np.mean(tf)

    n = len(tf)
    t = np.linspace(0, n , n ) / 24
    f = fs * np.linspace(0,n//2,n//2)/n


    fft = np.fft.fft(tf)
    fft_mean = np.fft.fft(tf_mean)

    fft_mag = np.abs(fft / n)
    fft_mean_mag = np.abs(fft_mean / n)

    th_mean = np.mean(fft_mean_mag) + 3 * np.std(fft_mean_mag)
    th = np.mean(fft_mag) + 3 * np.std(fft_mag)

    cnt = 0
    cnt_mean = 0

    for i in range(0,n):
        if fft_mag[i] > th:
            cnt += 1
            fft[i] = 0
        if fft_mean_mag[i] > th_mean:
            cnt_mean += 1
            fft_mean[i] = 0

    tf = np.fft.ifft(fft).real
    tf_mean = np.fft.ifft(fft_mean).real

    fig, axs = plt.subplots(2,2, figsize = (24, 22))
    fig.suptitle('Filtrare semnal normalizat si nenormalizat')

    axs[0][0].plot(t, tf)
    axs[0][0].set(xlabel = 'Timp (zile)', ylabel = 'Numar de masini', title = ('Semnal nenormalizat fara frecvente mari'))
    axs[0][0].grid(True)

    axs[0][1].plot(t, tf_mean)
    axs[0][1].set(xlabel = 'Timp (zile)', ylabel = 'Numar de masini', title = ('Semnal normalizat fara frecvente mari'))
    axs[0][1].grid(True)

    axs[1][0].plot(t,origin,color = 'b')
    axs[1][0].plot(t,tf, color = 'green')
    axs[1][0].plot(t,tf_mean, color = 'red')
    axs[1][0].set(xlabel = 'Timp (zile)', ylabel = 'Numar de masini', title = ('Semnal original vs normalizat filtrat si nenormalizat filtrat'))
    axs[1][0].grid(True)

    axs[1][1].plot(f, (np.abs(np.fft.fft(origin/n)))[:n // 2], color = 'black')
    axs[1][1].set(xlabel = 'Frecventa', ylabel = 'Magnitudine', title = ('FFT original si filtrele'))
    axs[1][1].axhline(th, color='red', linestyle='--', label = 'media + 2 deviatii standard semnal nenormalizat')
    axs[1][1].axhline(th_mean, color='blue', linestyle='--', label = 'media + 2 deviatii standard semnal normalizat')
    axs[1][1].legend()
    axs[1][1].grid(True)

    plt.savefig('i.pdf')
    plt.tight_layout()
    plt.show()

d(train_file)
e(train_file)
f(train_file)
g(train_file)
h()
i(train_file)