import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Taylor vs Pade - 0y logaritmica')

pi = np.pi

t = np.linspace(-pi/2, pi/2, 500)

def pade(alpha):
    return (alpha - 7 * (alpha ** 3) / 60) / (1 + (alpha ** 2) / 20)

axs[0].plot(t, np.sin(t))
axs[0].grid(True)
axs[0].set_ylabel('Sin')

axs[1].plot(t, t)
axs[1].grid(True)
axs[1].set_ylabel('Sin(x) = x')

axs[2].plot(t, pade(t))
axs[2].grid(True)
axs[2].set_ylabel('Pade')

fig.tight_layout()
# plt.yscale('log')
plt.savefig('8a.pdf')
plt.show()

taylor_er = np.abs(np.sin(t) - t)
pade_er = np.abs(np.sin(t) - pade(t))

plt.plot(t, taylor_er, color='green', label='Eroare Taylor')
plt.plot(t, pade_er, color='red', label='Eroare Pade')
plt.title('Erori Taylor vs Pade')
plt.xlabel('Alpha')
plt.ylabel('Eroare')
plt.grid(True)
plt.legend()
# plt.yscale('log')
plt.savefig('8b.pdf')
plt.show()