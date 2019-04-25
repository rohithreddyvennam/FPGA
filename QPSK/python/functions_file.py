import numpy as np
from time import sleep
import progressbar
import math

def decimalToBinary(decimalArray, size, noBits, binary2DArray):
	for i in range(size):
		temp = int(abs(decimalArray[i]))
		#print(temp)
		binary2DArray[i][noBits-1] = 0 if(decimalArray[i] >= 0) else 1
		#print(binary2DArray[i][noBits-1])

		for j in range(noBits-1):
			#print("i: "+str(i)+" j: "+str(j))
			binary2DArray[i][j] = temp%2
			temp = temp/2
			#print(binary2DArray[i][j])

def binaryToDecimal(binary2DArray, size, noBits, decimalArray):
	for i in range(size):
		
		sign = -2*(binary2DArray[i][noBits-1]) + 1
		#print(sign)

		temp = 0
		for j in range(noBits-1):
			temp = temp + (binary2DArray[i][j])*math.pow(2,j)

		temp = temp * sign
		decimalArray[i] = int(temp)
		#print(temp)

def calculateBER(input_bits, output_bits, size, noBits):

	#xor of input and output bits
	error_bits = np.logical_xor(input_bits, output_bits)
	#print(error_bits)

	#error
	error = np.sum(error_bits)
	#print(error)

	#BER
	BER = float(error)/(size * noBits)

	return BER

def qpskModulation(input_bits, size, noBits, serialm, modulated_output):
	print ('\nQPSK Modulation')

	# for printing ProgressBar
	bar = progressbar.ProgressBar(maxval=size, \
    widgets=[progressbar.Bar("#", '|', '|'), ' ', progressbar.Percentage()])
	bar.start()

	# sending 4 bits at a time
	k = int(noBits/4)

	for n in range(size):
		#print (n)
		bar.update(n+1)

		#print ('\n n: '+ str(n) +', '+str(in_discrete_signal[n]))
		for i in range(2):

			string = str(input_bits[n][4*i])+ '\n'
			serialm.write(str.encode(string))
			#print (string)  
			
			string = str(input_bits[n][4*i+1])+ '\n'
			serialm.write(str.encode(string))
			#print (string)  
			
			string = str(input_bits[n][4*i+2])+ '\n'
			serialm.write(str.encode(string))
			#print (string)
			
			string = str(input_bits[n][4*i+3])+ '\n'
			serialm.write(str.encode(string))
			#print (string) 

			#sleep(.000005) # Delay for one tenth of a second

			str_in =  serialm.readline()
			#print (str_in)
			sign = -2*int(str_in)+1

			str_in =  serialm.readline()
			#print (str_in)
			a = int(str_in)*sign
			
			str_in =  serialm.readline()
			#print (str_in)
			sign = -2*int(str_in)+1

			str_in =  serialm.readline()
			#print (str_in)
			b = int(str_in)*sign
			
			str_in =  serialm.readline()
			#print (str_in)
			sign = -2*int(str_in)+1

			str_in =  serialm.readline()
			#print (str_in)
			c = int(str_in)*sign

			str_in =  serialm.readline()
			#print (str_in)
			sign = -2*int(str_in)+1

			str_in =  serialm.readline()
			#print (str_in)
			d = int(str_in)*sign
			
			modulated_output[2*(k*n+i)] = (a+1j*b)/np.sqrt(2)
			modulated_output[2*(k*n+i)+1] = (c+1j*d)/np.sqrt(2)

	bar.finish()


def qpskDemodulation(received_signal, size, noBits, serialD, output_bits):
	print ('\nQPSK Demodulation')

	# for printing ProgressBar
	bar = progressbar.ProgressBar(maxval=size, \
    widgets=[progressbar.Bar("#", '|', '|'), ' ', progressbar.Percentage()])

	bar.start()
	k = int(noBits/4)
	for count in range(size):
		#print (count)
		bar.update(count+1)

		for i in range(k):

			x_real = 1 if received_signal[2*(k*count+i)].real > 0 else -1
			string = str(x_real)+ ' \n'
			serialD.write(str.encode(string))
			#print (' real : '+ string) 

			x_imag = 1 if received_signal[2*(k*count+i)].imag > 0 else -1
			string = str (x_imag)+ '\n'
			serialD.write(str.encode(string))
			#print (' imag : '+ string) 

			y_real = 1 if received_signal[2*(k*count+i)+1].real > 0 else -1
			string = str (y_real)+ '\n'
			serialD.write(str.encode(string))
			#print (' real : '+ string) 

			y_imag = 1 if received_signal[2*(k*count+i)+1].imag > 0 else -1
			string = str (y_imag)+ '\n'
			serialD.write(str.encode(string))
			#print (' imag : '+ string) 
		 
			#sleep(.000005) # Delay for one tenth of a second

			#Reading output
			str_in =  serialD.readline()
			#print (str_in)
			output_bits[count][4*i] = int(str_in)

			str_in =  serialD.readline()
			#print (str_in)
			output_bits[count][4*i+1] = int(str_in)

			str_in =  serialD.readline()
			#print (str_in)
			output_bits[count][4*i+2] = int(str_in)

			str_in =  serialD.readline()
			#print (str_in)
			output_bits[count][4*i+3] = int(str_in)

	bar.finish()