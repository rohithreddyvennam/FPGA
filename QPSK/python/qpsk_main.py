import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from playsound import playsound
import functions_file
import serial
import math


### Sinsoidal Waves 
f_0 = 200.0
samples = 200
t = np.linspace(-5/f_0,5/f_0,samples)
input_signal = np.cos(2*np.pi*f_0*t) 

# Common Parameters
noBits = 8
size = len(input_signal)

### Converting into Discrete values
mfactor = math.pow(2,(noBits-1))-1
in_discrete_signal = np.round(input_signal*(mfactor)) #input decimalArray

input_bits = np.zeros((size, noBits), dtype = int) #input binary2DArray
functions_file.decimalToBinary(in_discrete_signal, size, noBits, input_bits)


########################## Modulation ################################

# calling Arduino 
serialM = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

# Required Modulation Parameters 
modulated_output = [10+1j*10]*4*size
functions_file.qpskModulation(input_bits, size, noBits, serialM, modulated_output)

snr_dB = 20
snr = 10**(snr_dB/10) 
noise = (1.0/math.sqrt((2*snr)))*(np.random.normal(0,1,4*size) + 1j*np.random.normal(0,1,4*size))
rx = modulated_output + noise
#subplots
plt.plot(rx.real, rx.imag, '.')
plt.title('Modulated QPSK Signal')
plt.xlabel(' In Phase')
plt.ylabel(' Quadrature Phase')
plt.axhline(0,color='k')
plt.axvline(0,color='k')
plt.grid()
plt.draw()
plt.pause(0.001)


########################## Demodulation ################################

### calling Arduino 
serialD = serial.Serial('/dev/ttyACM2', 9600) # Establish the connection on a specific port

### Demodulation Parameters
output_bits = np.zeros((size, noBits), dtype = int)
functions_file.qpskDemodulation(rx, size, noBits, serialD, output_bits)

### output signal
out_discrete_signal = [0]*size
functions_file.binaryToDecimal(output_bits, size, noBits, out_discrete_signal)
output_signal = [x/mfactor for x in out_discrete_signal]


plt.subplot(2, 1, 1)
plt.plot(input_signal)
plt.title('Input signal')
plt.ylabel('$x(t)$')
plt.grid()# minor

plt.subplot(2, 1, 2)
plt.plot(output_signal)
plt.title('Output Signal')
plt.ylabel('$x(t)$')
plt.grid()# minor
plt.show()