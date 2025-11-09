import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
e = np.e
f = 25
fs = 8
new_fs = 80

def semnal_sinus(a,f,t,o):
    return a * np.sin(2 * pi * f * t + o)

t = np.linspace(0,1,2000)
ts = np.linspace(0,1, new_fs, endpoint= False)

semnal1 = semnal_sinus(1, f, t, 0)
semnal1_esantionat = semnal_sinus(1, f, ts, 0)

fig, axs = plt.subplots(4,1, figsize= (20,12))
fig.suptitle('Fenomenul de aliere')

axs[0].plot(t,semnal1)
axs[0].set(xlabel = ('Timp'), ylabel = ('Frecventa'), title = (f'Semnal original {f}hz'))
axs[0].grid(True)

axs[1].plot(t,semnal1)
axs[1].scatter(ts,semnal1_esantionat, color ='black')
axs[1].set(xlabel = ('Timp'), ylabel = ('Frecventa'), title = (f'Semnal original {f}hz, esantionat cu frecventa {new_fs}'))
axs[1].grid(True)

semnal2 = semnal_sinus(1, f + fs, t, 0)
semnal2_esantionat = semnal_sinus(1, f + fs, ts, 0)

axs[2].plot(t,semnal2,'g')
axs[2].scatter(ts,semnal2_esantionat, color = 'black')
axs[2].set(xlabel = ('Timp'), ylabel = ('Frecventa'), title = (f'Semnal cu frecventa {f + fs}hz, esantionat cu frecventa {new_fs}'))
axs[2].grid(True)

semnal3 = semnal_sinus(1, f - 3 * fs, t, 0)
semnal3_esantionat = semnal_sinus(1, f - 3 *  fs, ts, 0)

axs[3].plot(t,semnal3, 'r')
axs[3].scatter(ts,semnal3_esantionat, color = 'black')
axs[3].set(xlabel = ('Timp'), ylabel = ('Frecventa'), title = (f'Semnal cu frecventa {f - 3 * fs}hz, esantionat cu frecventa {new_fs}'))
axs[3].grid(True)


plt.tight_layout()
plt.savefig('3.pdf')
plt.show()
