import matplotlib.pyplot as plt
import numpy as np

n = 1000
pi = np.pi

def get_trend(x):
    return 2 * ((x-0.2)*(x-0.45)) ** 2 + 3 * (x-0.2)*(x-0.45) + 1

def get_sezon(t):
    return 2 * np.sin(2 * pi * t * 15 + 5) + np.sin(2 * pi * t * 5 + 2)

def get_zgomot(x):
    return np.random.normal(0,.3, size = x)

def a(t,s,tr,sez,var):
    fig, axs = plt.subplots(2,2,figsize = (16,12))
    fig.suptitle('Serie de timp alcatuita din 3 componente')

    axs[0,0].plot(t,s)
    axs[0,0].set(xlabel = 'Time', ylabel = 'Value', title = 'Serie de timp compusa')
    axs[0,0].grid(True)

    axs[0,1].plot(t,tr)
    axs[0,1].set(xlabel = 'Time', ylabel = 'Value', title = 'Trend')
    axs[0,1].grid(True)

    axs[1,0].plot(t,sez)
    axs[1,0].set(xlabel = 'Time', ylabel = 'Value', title = 'Sezon')
    axs[1,0].grid(True)

    axs[1,1].plot(t,var)
    axs[1,1].set(xlabel = 'Time', ylabel = 'Value', title = 'Variatii mici')
    axs[1,1].grid(True)

    plt.tight_layout()
    plt.savefig('a.pdf')
    plt.show()

def b(s,t):
    s = s - np.mean(s)
    x = np.correlate(s,s,'full')
    x = x[n-1:]
    x = x/x[0]

    x2 = []
    for i in range(n):
        cov = np.sum(s[i:]*s[:n-i])
        cov = cov/((n-i)*(np.var(s)))
        x2.append(cov)

    fig,axs = plt.subplots(1,2, figsize = (14,12))
    fig.suptitle('Autocorelatie')

    axs[0].plot(t,x)
    axs[0].set(title = 'np.correlate', xlabel = 'Lag', ylabel = 'Autocorelatie')
    axs[0].grid(True)

    axs[1].plot(t,x2)
    axs[1].set(title = r"Autocorelare conform formulei:  $\hat{R}(k)=\frac{1}{(n-k)\sigma^{2}}\sum_{t=1}^{n-k}(X_t-\mu)(X_{t+k}-\mu)$", xlabel = 'Lag', ylabel = 'Autocorelatie')
    axs[1].grid(True)

    plt.tight_layout()
    plt.savefig('b.pdf')
    plt.show()

def c(s, t, plot, vec = ([5,10], [50,100], [100, 225], [200,600])):
    p_m = vec
    final_pred = []
    final_pred_c = []

    for k in range(len(p_m)):
        p,m = p_m[k]
        predictions = []
        predictions_ones = []


        for i in range(900,1000):
            y = s[i-m+1 : i+1]
            col = []
            for j in range(1,p+1):
                col.append(s[i-m-j+1 : i-j+1])

            Y = np.column_stack(col)

            col.append(np.ones(m))
            Y_ones = np.column_stack(col)

            x = np.linalg.lstsq(Y, y)[0]
            x_ones = np.linalg.lstsq(Y_ones, y, rcond=None)[0]


            y2 = s[i-p : i]
            y2 = y2[::-1]

            y3 = y2.copy()
            y3 = np.append(y3, 1)

            predictions.append(x.T @ y2)
            predictions_ones.append(x_ones.T @ y3)

        final_pred.append(predictions)
        final_pred_c.append(predictions_ones)

    l = len(p_m)
    fig, axs = plt.subplots(l,figsize = (24,5 * l),gridspec_kw={'hspace': 0.1 * l})
    fig.suptitle('AR')

    for i in range(len(final_pred)):
        p,m = p_m[i]
        axs[i].plot(t,s, linewidth = 2, label = 'Semnal Original')
        axs[i].plot(t[900:],final_pred[i],color = 'red', linewidth = 0.5, label = 'Predictie')
        axs[i].plot(t[900:],final_pred_c[i],color = 'black', linewidth = 0.5, label = 'Predictie cu cloana de 1')
        axs[i].grid(True)
        axs[i].set(title = f'p = {p}, m = {m}', xlabel = 'Time', ylabel = 'Signal')

    plt.legend()
    plt.savefig('c.pdf')
    plt.show()

    fig, axs = plt.subplots(4, figsize = (20, 10))
    fig.suptitle('Corelatie')

    for k in range(len(final_pred)):
        p = final_pred[k]
        p = p - np.mean(p)
        x = np.correlate(p, p, 'full')
        pred_len = len(p)
        x = x[pred_len - 1:]
        x = x / x[0]

        axs[k].plot(t[900:], x, label = 'corelatie')
        axs[k].set(title='np.correlate', xlabel='Lag', ylabel='Autocorelatie')
        axs[k].grid(True)

    plt.legend()
    plt.savefig('c_corelatie.pdf')
    plt.show()

    return final_pred


def d(s,t):
    p_values = range(1, 101)
    m_values = range(10, 501, 10)

    best_mae = float('inf')
    best_p = None
    best_m = None
    mae_results = []
    best_pred = []

    for p in p_values:
        for m in m_values:
            if m <= p:
                continue
            pred = []

            for i in range(900, 1000):
                y = s[i - m + 1: i + 1]
                col = []
                for j in range(1, p + 1):
                    col.append(s[i - m - j + 1: i - j + 1])

                Y = np.column_stack(col)

                x = np.linalg.lstsq(Y, y)[0]

                y2 = s[i - p: i]
                y2 = y2[::-1]

                pred.append(x.T @ y2)

            mae = np.mean(np.abs(np.array(pred) - s[900:]))
            mae_results.append((p, m, mae))

            if mae < best_mae:
                best_mae = mae
                best_p = p
                best_m = m
                best_pred = pred

    plt.figure(figsize = (24,10))


    plt.plot(t, s, linewidth=2, label = 'Semnal Original')
    plt.plot(t[900:], best_pred, color='red', linewidth=1, label = 'Predictie')
    plt.title(f'Best parameters: p = {best_p}, m = {best_m}, MAE = {round(best_mae,6)}')
    plt.xlabel('Time')
    plt.ylabel('Signal')

    plt.grid(True)

    plt.legend()
    plt.tight_layout()
    plt.savefig('d.pdf')
    plt.show()

t = np.linspace(0,1,n)
trend = get_trend(t)
sezon = get_sezon(t)
variatii_mici = get_zgomot(n)

serie = trend + sezon + variatii_mici

# a(t, serie, trend, sezon, variatii_mici)
# b(serie,t)
c(serie,t, True)
# d(serie,t)