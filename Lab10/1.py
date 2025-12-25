import matplotlib.pyplot as plt
import numpy as np
from l1regls import l1regls
import cvxopt as cv

n = 1000
pi = np.pi

def get_trend(x):
    return 2.2 * ((x-0.45)*(x-1.75)) ** 2 + 3 * (x-0.45)*(x-1.75) + 1

def get_sezon(t):
    return 2 * np.sin(2 * pi * t * 10 + 3.7) + 1.5 * np.sin(2 * pi * t * 5 + 2.3)

def get_zgomot(x):
    return np.random.normal(0,.45, size = x)

def _2(x, t, m = 35, p = 12):
    pred = []
    for k in range(900,1000):
        
        Y = []
        for i in range(0,m):
            row = x[k - i - p - 1: k - i]
            Y.append(row)
        Y = np.array(Y)
        
        y = x[k - 1: k - m - 1: -1]
        y = np.array(y)
        
        X = np.linalg.lstsq(Y, y, rcond = None)[0]
        
        y2 = np.array(x[k-p-1: k])
        pred.append(X.T @ y2)
    
    mae = np.mean(np.abs(np.array(pred) - x[900:]))

    
    plt.figure(figsize=(15,10))
    plt.title(f'Model AR cu m = {m}, p = {p}, MAE = {mae}')
    plt.plot(t, x, c ='lightblue', linewidth = 1, label = 'Serie originala')
    plt.plot(t[900:1000], pred, '--', c = 'r', linewidth = 0.5, label = 'Serie prezisa de AR')
    plt.xlabel('Time')
    plt.ylabel('Value')
    
    plt.legend()
    plt.savefig('2.pdf')
    plt.show()

def _3(x,t,p_lim, max_p = 75):
    
    Y = []
    y = []
    
    for i in range(max_p, 900):
        row = x[i - max_p: i]
        Y.append(row)
        y.append(x[i])
    
    Y = np.array(Y)
    y = np.array(y)
    
    viz = []
    maes = []
    best_global_mae = np.inf
    best_global_pred = []
    best_global_p = 0
    best_global_coeffs = np.zeros(max_p)
    
    for step in range(p_lim):
        best_mae = np.inf
        best_idx = -1
        best_pred = []

        
        for i in range(max_p):
            if i in viz:
                continue
                
            viz.append(i)
            Y_subset = Y[:, viz]
            
            X = np.linalg.lstsq(Y_subset, y, rcond=None)[0]
            
            pred = []
            for k in range(900, 1000):
                y2 = x[k-max_p:k]
                y_pred = y2[viz]
                pred.append(X.T @ y_pred)
            
            mae = np.mean(np.abs(np.array(pred) - x[900:]))
            
            if mae < best_mae:
                best_mae = mae
                best_idx = i
                best_pred = pred.copy()
            
            viz.pop()
        
        if best_idx != -1:
            viz.append(best_idx)
            maes.append(best_mae)
            
            if best_mae < best_global_mae:
                best_global_mae = best_mae
                best_global_pred = best_pred.copy()
                best_global_p = step + 1
                
                Y_subset = Y[:, viz]
                X = np.linalg.lstsq(Y_subset, y, rcond=None)[0]
                best_global_coeffs[viz] = X
    
    fig, axs = plt.subplots(3,figsize = (15,21))
    fig.suptitle('Greedy select for p')
    
    axs[0].plot(t, x, c = 'lightblue', linewidth = 1.5, label = 'Original series')
    axs[0].plot(t[900:], best_pred, c = 'red', linewidth = 0.4, label = f'Best prediction')
    
    mae =  np.mean(np.abs(np.array(best_pred) - x[900:]))
    axs[0].set(title = f'Best greedy, p = {viz}, mae = {mae}', xlabel = 'Time', ylabel = 'Value')
    axs[0].grid(True)
    axs[0].legend()
    
    axs[1].plot(range(1,p_lim + 1), maes, 'o')
    axs[1].set( title = 'MAE error evolution', xlabel = 'p', ylabel = 'MAE')
    axs[1].grid(True)
    
    axs[2].plot(t, x, c='lightblue', linewidth=1.5, label='Original series')
    axs[2].plot(t[900:], best_global_pred, c='green', linewidth=0.4, label=f'Best global prediction')
    axs[2].set(title=f'Best global model, p = {best_global_p}, MAE = {best_global_mae}', xlabel='Time', ylabel='Value')
    axs[2].grid(True)
    axs[2].legend()
    
    plt.savefig(f'3_greedy_p={p_lim}.pdf')
    plt.show()
    
    return best_global_coeffs
    
def _3_lasso(x, t, max_p=75):
    
    Y = []
    y = []
    
    for i in range(max_p, 900):
        row = x[i - max_p: i]
        Y.append(row)
        y.append(x[i])
    
    Y = np.array(Y)
    y = np.array(y)
    
    Y = cv.matrix(Y)
    y = cv.matrix(y)
    
    X = l1regls(Y, y)
    X = np.array(X).flatten()
    
    threshold = 1e-5
    X[np.abs(X) < threshold] = 0
    
    non_zero = np.sum(np.abs(X) > 0)

    pred = []
    for k in range(900, 1000):
        y2 = x[k - max_p: k]
        pred.append(X.T @ y2)
    
    mae = np.mean(np.abs(np.array(pred) - x[900:]))
    
    fig, axs = plt.subplots(2, figsize=(15, 16))
    fig.suptitle('L1 - Lasso zeros')
    
    axs[0].plot(t, x, c='lightblue', linewidth=1.5, label='Original series')
    axs[0].plot(t[900:], pred, c='red', linewidth=0.4, label='Lasso prediction')
    axs[0].set(title=f'Lasso AR Model, p={max_p}, MAE={mae}, Non-zero: {non_zero}/{max_p}', xlabel='Time', ylabel='Value')
    axs[0].grid(True)
    axs[0].legend()
    
    axs[1].scatter(range(max_p), X, c = 'red', s = 10)    
    axs[1].plot(range(max_p), X, c = 'b' ,linewidth=1.0, label = 'Coefficients')
    axs[1].set(title=f'Coefficients Non-zero: {non_zero}/{max_p}', xlabel='Lag', ylabel='Coefficient')
    axs[1].grid(True)
    axs[1].legend()
    
    plt.savefig(f'3_lasso_p={max_p}.pdf')
    plt.show()
    
    return X

def _4(v):
    v = np.array(v)
    n = len(v)
    C = np.zeros((n,n))
    
    s = 1
    e = 0
    C[:,n-1] = -v
    
    for i in range(1 , n):
        C[i,i-1] = 1
    
    eig = np.linalg.eigvals(C)
    return eig
            
        
def _5(coef):
    rad = _4(coef)
    rad_abs = np.abs(rad)
    
    is_stationary = True
    for i in rad_abs:
        if i > 1:
            is_stationary = False
            break
    
    fig, axs = plt.subplots(figsize=(15, 16))
    fig.suptitle('Stationaritatea seriei')
    
    t = np.linspace(0, 2*np.pi, 200)
    axs.plot(np.cos(t), np.sin(t), linewidth=2, label='Cerc unitate')
    
    colors = ['green' if mod > 1 else 'red' for mod in rad_abs]
    axs.scatter(rad.real, rad.imag, c=colors, s=20, label='Radacini')
    
    axs.axhline(y=0, color='black', linewidth=1)
    axs.axvline(x=0, color='black', linewidth=1)
    
    axs.grid(True)
    axs.set(xlabel = 'Parte reala', ylabel = 'Parte imaginara', title = f'Radacinile pe cercul unitate, seria este stationara: {is_stationary}')
    axs.legend()
    axs.axis('equal')
    
    # plt.savefig('5_lasso.pdf')
    plt.show()
    
t = np.linspace(0,1,n)
trend = get_trend(t)
sezon = get_sezon(t)
variatii_mici = get_zgomot(n)

serie = trend + sezon + variatii_mici

# _2(serie,t)
# _3(serie,t,25)
# _3_lasso(serie,t,25)

# greedy = _3(serie,t,25,25)
# lasso = _3_lasso(serie,t,25)

# fig, axs = plt.subplots(2,figsize = (15,16))
# fig.suptitle('Greedy vs Lasso coefficients')

# non_zero_greedy = np.sum(np.abs(greedy) > 0)
# axs[0].stem(range(25), greedy, linefmt='b-', markerfmt='bo')
# axs[0].set(title=f'Greedy Coefficients: {non_zero_greedy}/25 non-zero', xlabel='Lag', ylabel='Coefficient')
# axs[0].grid(True)

# non_zero_lasso = np.sum(np.abs(lasso) > 0)
# axs[1].stem(range(25), lasso, linefmt='r-', markerfmt='ro')
# axs[1].set(title=f'Lasso Coefficients: {non_zero_lasso}/25 non-zero', xlabel='Lag', ylabel='Coefficient')
# axs[1].grid(True)

# plt.savefig('greedy_vs_lasso.pdf')
# plt.show()

v_coef = [3,2,5,2.3,4,5,9]
# rad = _4(v_coef)
# print(rad)

# _5(v_coef)

# greedy = _3(serie,t,25)
# _5(greedy)

# lasso = _3_lasso(serie,t,25)
# _5(lasso)