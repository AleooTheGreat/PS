import numpy as np
import sounddevice as sd

pi = np.pi
t = np.linspace(100,300,1600 * 15)

def semnal_sin(A, t, f, omega):
    return A * np.sin(2 * pi * t * f + omega)

semnal1 = semnal_sin(2,t,100,0)
semnal2 = semnal_sin(2,t,1000, 0)

semnal_final = np.concatenate([semnal1, semnal2])


sd.play(semnal_final,44100)
sd.wait()
