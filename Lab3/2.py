import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pi = np.pi
e = np.e

def semnal_sinusoidal(a,t,f,omega):
    return a * np.sin(2 * pi * t * f + omega)

def z(list_omega, t, semnal):

    ans = []

    for i in list_omega:
        aux = semnal * e **(-2 * pi * 1j * i * t)
        ans.append(aux)

    return ans

class SignalAnimations:
    def __init__(self, refresh_ms=300, use_blit=False):
        self.refresh_ms = refresh_ms
        self.use_blit = use_blit

    def figure1(self, t, semnal, y_complex):
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('Figura 1 (animatie, refresh mic)')

        axs[0].plot(t, semnal, color='green')
        axs[0].set_xlabel('Timp')
        axs[0].set_ylabel('Amplitudine')
        axs[0].grid(True)

        axs[1].plot(y_complex.real, y_complex.imag, color='blue')
        axs[1].set_xlabel('Real')
        axs[1].set_ylabel('Imaginar')
        axs[1].grid(True)

        pt_time, = axs[0].plot([], [], 'o', color='red')
        vline_time, = axs[0].plot([], [], color='red')
        pt_complex, = axs[1].plot([], [], 'o', color='red')
        line_complex, = axs[1].plot([], [], color='red')

        def _init():
            pt_time.set_data([], [])
            vline_time.set_data([], [])
            pt_complex.set_data([], [])
            line_complex.set_data([], [])
            return pt_time, vline_time, pt_complex, line_complex

        def _update(i):
            x = t[i]
            y_t = semnal[i]
            pt_time.set_data([x], [y_t])
            vline_time.set_data([x, x], [0, y_t])

            xr = y_complex[i].real
            xi = y_complex[i].imag
            pt_complex.set_data([xr], [xi])
            line_complex.set_data([0, xr], [0, xi])
            return pt_time, vline_time, pt_complex, line_complex

        anim = FuncAnimation(
            fig, _update, frames=len(t), init_func=_init,
            interval=self.refresh_ms, blit=self.use_blit, repeat=True
        )
        return fig, anim

    def figure2(self, t, z_vals, omega):
        fig2, axs2 = plt.subplots(2, 2, figsize=(24, 10))
        fig2.suptitle('Figura 2 (animatie, refresh mic)')
        axs2_flat = axs2.ravel()

        pts = []
        lines = []

        for i, w in enumerate(omega):
            zi = z_vals[i]
            ax = axs2_flat[i]

            z_mean_real = np.mean(zi.real)
            z_mean_imag = np.mean(zi.imag)
            ax.plot(zi.real, zi.imag, color='green')
            ax.plot(z_mean_real, z_mean_imag, 'o', color='black')
            ax.plot([0, z_mean_real], [0, z_mean_imag], color='black')
            ax.set(xlim=(-1, 1), ylim=(-1, 1), xlabel='Real', ylabel='Imaginar', title=f'w = {w}')
            ax.grid(True)

            pt, = ax.plot([], [], 'o', color='red')
            ln, = ax.plot([], [], color='red')
            pts.append(pt)
            lines.append(ln)

        def _init():
            for pt, ln in zip(pts, lines):
                pt.set_data([], [])
                ln.set_data([], [])
            return (*pts, *lines)

        def _update(i):
            for idx in range(len(omega)):
                c = z_vals[idx][i]
                xr, xi = c.real, c.imag
                pts[idx].set_data([xr], [xi])
                lines[idx].set_data([0, xr], [0, xi])
            return (*pts, *lines)

        anim = FuncAnimation(
            fig2, _update, frames=len(t), init_func=_init,
            interval=self.refresh_ms, blit=self.use_blit, repeat=True
        )
        return fig2, anim

t = np.linspace(0,1,200)
semnal = semnal_sinusoidal(1,t,5,0)

y = semnal * e **(-2 * pi * 1j * t)

# Figura 1
fig, axs = plt.subplots(1,2, figsize = (12,5))
fig.suptitle('Figura 1')

axs[0].plot(t,semnal, color = 'green')
axs[0].plot(t[121], semnal[121], 'o' ,color = 'red')
axs[0].plot([t[121],t[121]], [0,semnal[121]], color = 'red')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Amplitudine')
axs[0].grid(True)

axs[1].plot(y.real,y.imag)
axs[1].plot(y[121].real, y[121].imag, 'o' ,color = 'red')
axs[1].plot([0,y[121].real], [0,y[121].imag], color = 'red')
axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imaginar')
axs[1].grid(True)

plt.tight_layout()
plt.savefig('2_figura1.pdf')
plt.show()

# Figura 2
omega = [1,2,5,7]
z = z(omega,t, semnal)

fig2, axs2 = plt.subplots(2,2, figsize = (24,10))
fig2.suptitle('Figura 2')

for i in range(0,4):

    z_mean_real = np.mean(z[i].real)
    z_mean_imag = np.mean(z[i].imag)


    axs2[i // 2][i % 2].plot(z[i].real, z[i].imag, color = 'green')
    axs2[i // 2][i % 2].plot(z_mean_real, z_mean_imag, 'o', color = 'black')
    axs2[i // 2][i % 2].plot([0,z_mean_real], [0,z_mean_imag], color = 'black')
    axs2[i // 2][i % 2].set(xlim=(-1, 1), ylim=(-1, 1), xlabel='Real', ylabel='Imaginar', title = f'w = {omega[i]}')
    axs2[i // 2][i % 2].grid(True)

plt.tight_layout()
plt.savefig('2_figura2.pdf')
plt.show()

# Gif-uri
animator = SignalAnimations(refresh_ms=175, use_blit=False)

fig1_anim, anim1 = animator.figure1(t, semnal, y)
plt.tight_layout()
plt.show()

fig2_anim, anim2 = animator.figure2(t, z, omega)
plt.tight_layout()
plt.show()