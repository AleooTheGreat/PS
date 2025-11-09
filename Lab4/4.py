import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel, ylabel

# Conform formulei Nyquist-Shannon trebuie sa avem fs >= 2 * B. In problema noastra avem frecvente intre 40hz si 200hz.
# Deci cea mai mare frecventa pe care trebuie sa o putem capta este 200hz => B = 200hz. Asadar trebuie sa avem frecventa
# minima 400hz ca sa putem capta toate componentele de freceventa pe care intrumentul le poate produce.

pi = np.pi

def semnal_sinus(a,f,t,o):
    return a * np.sin(2 * pi * f * t + o)

def get_semnal(t):
    return semnal_sinus(1,40, t, 0) + semnal_sinus(1,200,t,0) + semnal_sinus(1,100,t,0) + semnal_sinus(1,150,t,0)

t = np.linspace(0,1,2000)
ts_corect = np.linspace(0,1,400, endpoint= False)
ts_gresit = np.linspace(0,1,100, endpoint= False)

semnal = get_semnal(t)
semnal_esantionat_corect = get_semnal(ts_corect)
semnal_esantionat_gresit = get_semnal(ts_gresit)

semnal_150 = semnal_sinus(1,150,t,0)


fig, axs = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Comparatie esantionare')

axs[0].plot(t, semnal, color = 'lightblue', label = 'semnal contrabas')
axs[0].scatter(ts_corect, semnal_esantionat_corect, color = 'black')
axs[0].plot(t, semnal_150, color = 'red', label = 'semnal 150 hz')
axs[0].set(xlabel = 'Timp', ylabel = ('Frecventa'), title = ('Semnal contrabas esantionat corect (fs >= 2B)'))
axs[0].legend()


axs[1].plot(t, semnal, color = 'lightblue', label = 'semnal contrabas')
axs[1].scatter(ts_gresit, semnal_esantionat_gresit, color = 'black')
axs[1].plot(t, semnal_150, color = 'red', label = 'semnal 150hz')
axs[1].set(xlabel = ('Timp'), ylabel = ('Frecventa'), title = ('Semnal contrabas esantionat gresit (fs < 2B)'))
axs[1].legend()

plt.savefig('4.pdf')
plt.tight_layout()
plt.show()