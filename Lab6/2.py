import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
t = np.arange(0,100)

fig, axs = plt.subplots(2, 2, figsize=(20, 24))
fig.suptitle('x[n] aleator')

for i in range(0,4):
    axs[i // 2][i % 2].plot(t, x, c='red')
    axs[i // 2][i % 2].set(xlabel=(f't = [0:100]'), ylabel=('Value'), title=(f'Iteratia {i}'))
    axs[i // 2][i % 2].grid(True)
    if i < 3:
        x = x * x

fig.savefig('2_aleator.pdf')
plt.show()

x = np.zeros(100)
x[0:25] = 1

fig, axs = plt.subplots(2, 2, figsize=(20, 24))
fig.suptitle('x[n] rectangular')

for i in range(0,4):
    axs[i // 2][i % 2].plot(t, x, c='red')
    axs[i // 2][i % 2].set(xlabel=(f't = [0:100]'), ylabel=('Value'), title=(f'Iteratia {i}'))
    axs[i // 2][i % 2].grid(True)
    if i < 3:
        x = x * x

fig.savefig('2_rectangular.pdf')
plt.show()