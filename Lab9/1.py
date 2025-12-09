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

def triple(a_values, b_values, c_values, x, L, best_mae = np.inf, best_a = 0, best_b = 0, best_c = 0, best_s = np.zeros(n)):
    
    n = len(x)
    for a in a_values:
        for beta in b_values:
            for lamb in c_values:
                s = np.zeros(n)
                b = np.zeros(n)
                c = np.zeros(n)

                s[0] = x[0]
                b[0] = x[1] - x[0]

                mean_L = np.mean(x[:L])
                for i in range(L):
                    c[i] = x[i] - mean_L
                
                for i in range(1, n):
                    
                    c_fact = c[i-L] if i >= L else 0
                    
                    s[i] = a * (x[i] - c_fact) + (1-a) * (s[i-1] + b[i-1])
                    b[i] = beta * (s[i] - s[i-1]) + (1-beta) * b[i-1]
                    
                    if i >= L:
                        c[i] = lamb * (x[i] - s[i] - b[i-1]) + (1-lamb) * c[i-L]
                
                predictions = np.zeros(n-1)
                for i in range(1, n):
                    c_fact = c[i-L] if i >= L else 0
                    predictions[i-1] = s[i-1] + b[i-1] + c_fact
                    
                mae = np.mean(np.abs(x[1:] - predictions))
                
                if best_mae > mae:
                    best_mae = mae
                    best_a, best_b, best_c = a, beta, lamb
                    best_s = s.copy()
    return best_a, best_b, best_c, best_mae, best_s

def a(x, t):    
    alpha = 0.75
    n = len(x)
    s = np.zeros(n)
    s[0] = x[0]

    
    for i in range(1,n):
        s[i] = alpha * x[i] + (1-alpha) * s[i-1]    
        
        
    fig, axs = plt.subplots(2, figsize = (25, 15))
    fig.suptitle('Mediere exponentiala')
    
    axs[0].plot(t, x, color = 'lightblue', linewidth = 2, label = 'Serie Originala')
    axs[0].plot(t, s, color = 'black', linewidth = 0.5, label = 'Serie cu alpha = 0.75')
    axs[0].set(xlabel = 'Time', ylabel = 'Value', title = f'Mediere exponentiala cu Alpha = {0.75}')
    axs[0].legend()
    axs[0].grid(True)
        
    alphas = np.linspace(0.01, 0.99, 1000)
    best_m = np.inf
    best_a = 0
    best_s = np.zeros(n)
    
    for i in range(len(alphas)):
        a = alphas[i]
        s = np.zeros(n)
        s[0] = x[0]
        for j in range(1,n):
            s[j] = a * x[j] + (1 - a) * s[j-1]
        
        m = np.mean(np.abs(x[1:] - s[:-1]))

        if best_m > m:
            best_m = m
            best_a = a
            best_s = s.copy()

    axs[1].plot(t, x, color = 'lightblue', linewidth = 2, label = 'Serie originala')
    axs[1].plot(t, best_s, color = 'black', linewidth = 0.5, label = f'Serie cu cel mai bun MAE = {np.round(best_m,10)}')
    axs[1].set(xlabel = 'Time', ylabel = 'Value', title = f' Mediere exponentiala cu MAE = {np.round(best_m,10)} pentru Alpha = {best_a}')
    axs[1].legend()
    axs[1].grid(True)
    
    plt.savefig('2_me.pdf')
    
    fig, axs = plt.subplots(3, figsize = (25, 16), gridspec_kw={'hspace': 0.3})
    fig.suptitle('Mediere simple, dubla si tripla')
    
    best_s_simpla = best_s.copy()
    axs[0].plot(t, x, color = 'lightblue', linewidth = 2, label = 'Serie originala')
    axs[0].plot(t, best_s_simpla, color = 'black', linewidth = 0.5, label = f'Mediere exponentiala')
    axs[0].set(xlabel = 'Time', ylabel = 'Value', title = f' Mediere exponentiala cu MAE = {np.round(best_m,10)} pentru Alpha = {best_a}')
    axs[0].legend()
    axs[0].grid(True)    
    
    # Mediere exponentiala dubla
    search_values = np.linspace(0.01,0.99, 250)

    best_mae = np.inf
    best_a = 0
    best_b = 0
    best_s = np.zeros(n)
    
    for a in search_values:
        for beta in search_values:
            
            s = np.zeros(n)
            b = np.zeros(n)
            
            s[0] = x[0]
            b[0] = x[1] - x[0]
            
            for i in range(1,n):
                s[i] = a * x[i] + (1-a) * (s[i-1] + b[i-1])
                b[i] = beta * (s[i] - s[i-1]) + (1-beta) * b[i-1]
            
            predictions = s[:-1] + b[:-1]
            mae = np.mean(np.abs(x[1:] - predictions))
            
            if best_mae > mae:
                best_mae = mae
                best_a, best_b = a, beta
                best_s = s.copy()
                
    best_s_dubla = best_s.copy()
    axs[1].plot(t, x, color = 'lightblue', linewidth = 2, label = 'Serie originala')
    axs[1].plot(t, best_s_dubla, color = 'black', linewidth = 0.5, label = f'Mediere exponentiala dubla')
    axs[1].set(xlabel = 'Time', ylabel = 'Value', title = f' Mediere exponentiala cu MAE = {np.round(best_mae,10)} pentru Alpha = {best_a}, Beta = {best_b}')
    axs[1].legend()
    axs[1].grid(True)   
    
    # Mediere exponentiala tripla
    search_values = np.linspace(0.01,0.99, 10)
    L_values = [3,5,7]
    
    best_mae = np.inf
    best_a = 0
    best_b = 0
    best_c = 0
    best_l = 0
    best_s = np.zeros(n)
    
    for L in L_values:
        a,b,c,m,ss = triple(search_values,search_values,search_values,x,L)
        
        if m < best_mae:
            best_mae = m
            best_a = a
            best_b = b
            best_c = c
            best_l = L
            best_s = ss.copy()
    
    a_val = np.linspace(max(0.01,best_a - 0.1), min(0.99, best_a + 0.1), 30)
    b_val = np.linspace(max(0.01,best_b - 0.1), min(0.99, best_b + 0.1), 30)
    c_val = np.linspace(max(0.01,best_c - 0.1), min(0.99, best_c + 0.1), 30)

    a,b,c,m,ss = triple(a_val,b_val,c_val,x,best_l, best_mae, best_a, best_b, best_c, best_s.copy())
        
    if m < best_mae:
        best_mae = m
        best_a = a
        best_b = b
        best_c = c
        best_s = ss.copy()
    
    best_s_tripla = best_s.copy()
    axs[2].plot(t, x, color = 'lightblue', linewidth = 2, label = 'Serie originala')
    axs[2].plot(t, best_s_tripla, color = 'black', linewidth = 0.5, label = f'Mediere exponentiala tripla')
    axs[2].set(xlabel = 'Time', ylabel = 'Value', title = f' Mediere exponentiala cu MAE = {np.round(best_mae,10)} pentru Alpha = {best_a}, Beta = {best_b}, Lambda = {best_c}, L = {best_l}')
    axs[2].legend()
    axs[2].grid(True)
    
    plt.savefig('2_me_sdt.pdf')
    plt.show()



t = np.linspace(0,1,n)
trend = get_trend(t)
sezon = get_sezon(t)
variatii_mici = get_zgomot(n)

serie = trend + sezon + variatii_mici

a(serie, t)