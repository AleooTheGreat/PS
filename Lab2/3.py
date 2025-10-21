import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wv

def semnal_sinusoidal(t,f):
    return np.sin(2*np.pi*t*f)

def semnal_sawtooth(t,f):
    return 2 * (t * f - np.floor(1/2+t*f))

def semnal_square(t,f):
    return np.sign(np.sin(2 * np.pi * f * t))

t = np.linspace(100,300,1600 * 5) # 5 sec
sd.default.samplerate = 44100
#a
sin = semnal_sinusoidal(t,400)
sd.play(sin)
sd.wait()
print('Done sin')
#b

sin2 = semnal_sinusoidal(t,800)
sd.play(sin2)
sd.wait()
print('Done sin2')
#c

saw = semnal_sawtooth(t,240)
sd.play(saw,44100)
sd.wait()
print('Done sawtooth')

#d

semnal_sq = semnal_square(t,300)
sd.play(semnal_sq)
sd.wait()
print('Done square')

# Save + listen
wv.write('sawtooth_5_sec.wav', 44100, saw)
loaded_rate, loaded_data = wv.read('sawtooth_5_sec.wav')
