import numpy as np
import matplotlib.pyplot as plt

B_values = [1,2,0.1,10,-0.5]
t = np.linspace(-3, 3, 200)

for B in B_values:
    x = np.sinc(B * t) ** 2

    eps = 0.00001
    ts_values = [1, 1.5, 2, 4]

    fig, axs = plt.subplots(2,2, figsize = (20,24))
    fig.suptitle('Sinc^2(t), reconstructia sa si puncte de esantionare')

    for i in range(len(ts_values)):
        Ts = 1/ts_values[i]

        t_s1 = np.arange(0, -3 - eps, -Ts)
        t_s1 = np.flip(t_s1)

        t_s2 = np.arange(0, 3 + eps, Ts)
        t_s2 = t_s2[1:]

        t_s = np.concatenate((t_s1, t_s2))
        x_s = np.sinc(B * t_s) ** 2

        c_ts = []
        for t_sam in t_s:
            aux = t - t_sam
            aux = aux / Ts
            c_ts.append(np.sinc(aux))

        x_t = x_s.T @ c_ts

        axs[i // 2][i % 2].stem(t_s, x_s, linefmt = 'black', markerfmt = 'black')
        axs[i // 2][i % 2].plot(t, x, c = 'red')
        axs[i // 2][i % 2].plot(t, x_t, '--', c = 'green')
        axs[i // 2][i % 2].set(xlabel = (f't[s]'), ylabel = ('Amplitudine'), title = (f'Fs = {ts_values[i]} Hz'))
        axs[i // 2][i % 2].grid(True)


    plt.savefig(f'1_B={B}.pdf')
    plt.show()