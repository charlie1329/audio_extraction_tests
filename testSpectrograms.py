import numpy as np 
import scipy.io.wavfile as wav 
import matplotlib.pyplot as plt 
import scipy.signal as sig 
import sys


#Author: Charlie Street

# function for computing stft and then outputting the spectrogram
# input_path is the wav file to read from (the test file)
# ground_truth is the original guitar stem
def showSpectrogram(input_path, ground_truth):
	
	segment_size = 8192
	overlap = 7680

	# get the test spectrogram

	rate, data = wav.read(input_path)

	data = data.astype(float)

	f, t, Zxx = sig.stft(data,fs=rate,window='hann',nperseg=segment_size,noverlap=overlap)

	testMat = np.abs(Zxx)

	# get the ground truth spectrogram

	gtRate, gtData = wav.read(ground_truth)

	gtData = gtData.astype(float)

	gtF, gtT, gtZxx = sig.stft(gtData,fs=gtRate,window='hann',nperseg=segment_size,noverlap=overlap)
	
	gtMat = np.abs(gtZxx)

	# compare the two matrices

	totalElements = gtMat.shape[0] * gtMat.shape[1] #used for average later

	lms = 0.0

	for i in range(0,gtMat.shape[0]):
		for j in range(0,gtMat.shape[1]):
			lms += pow(gtMat[i,j]-testMat[i,j],2.0)

	lms /= totalElements # take average

	print("The lms error is: " + str(lms))



if __name__ == '__main__':
	
	if len(sys.argv) != 8:
		print('Incorrect number of input arguments')
	else:
		input_path = sys.argv[1]
		ground_truth = sys.argv[2]
		compareSpectrograms(input_path,ground_truth)