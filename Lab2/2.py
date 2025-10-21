import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def semnal_sinus(A, f, t, omega):
    return A * np.sin( 2 * pi * f * t + omega)

def calcul_gamma(x, SNR):
    z = np.random.normal(0, 1, len(x))
    norma_semnal = np.linalg.norm(x)
    norma_zgomot = np.linalg.norm(z)
    gamma = norma_semnal / (np.sqrt(SNR) * norma_zgomot)
    return gamma, z


t = np.linspace(0,0.1,200)

fig, axs = plt.subplots(4)
fig.suptitle('Semnale cu zgomot')

axs[0].plot(t,semnal_sinus(3,400,t,0))
axs[0].grid(True)
axs[0].set_ylabel('Semnal 400hz')

axs[1].plot(t,semnal_sinus(3,200,t,0))
axs[1].grid(True)
axs[1].set_ylabel('Semnal 200hz')

axs[2].plot(t,semnal_sinus(3,20,t,0))
axs[2].grid(True)
axs[2].set_ylabel('Semnal 20hz')

axs[3].plot(t,semnal_sinus(3,50,t,0))
axs[3].grid(True)
axs[3].set_ylabel('Semnal 50hz')

fig.supxlabel('Time')
plt.savefig('2_semnale_simple.pdf')
fig.tight_layout()
fig.show()

fig2, axs2 = plt.subplots(4)
semnal = semnal_sinus(3,200,t,0)

SNR = [0.1, 1, 10, 100]

for i in range(0,4):
    gamma, z = calcul_gamma(semnal, SNR[i])
    semnal_z= semnal + gamma * z

    axs2[i].plot(t, semnal_z)
    axs2[i].grid(True)
    axs2[i].set_ylabel(f'SNR = {SNR[i]}')

fig2.supxlabel('Time')
fig2.tight_layout()
plt.savefig('2_semnal_cu_zgomot.pdf')
plt.show()