## Script for reading txt files containing student essays
import numpy as np
from os import path


def Txt_Parser(file_name):
	'''Takes file name as input and returns relevant language structures.
	Sentences are seperated out and stores in a numpy array as a string of
	language structures (e.g., 'The Cat in the Hat is fat.' becomes
	[article,subject nount,verb,adjective]. In addition, the tense of the
	sentence is stored.'''

	#Let's check if the input file is actually a .txt file...
	_,extension = path.splitext(file_name)
	if extension != '.txt':
		print 'ERROR: input file not a .txt file'
		return
	else:
		print 'Input file is a .txt file. Success!'
		
	#Okie dokie...it's a .txt file alright
	#Let's open it!
	with open(file_name) as f:
		sentence_array = Splt_Txt_Into_Sentences(f)	

def Split_Txt_Into_Sentences(f):
	'''Actually does work of arranging contents of file into numpy arrays'''
	sentence_array = np.zeros(len(f))
	last_sentence = ' '
	for line in f:
		#Split lines into sentences. Carries over sentence to next line
		#if sentence does not end on current line
		sentences = line.split('.','!','?')
		iterator = 0
		for sentence in sentences:
			#If this is the first sentence, add last sentence from
			#previous line to it IF the last sentence did not end
			#on the previous line 
			if iterator == 0:
				sentence = last_sentence + sentence
			#If we are on the last sentence for the line, add this
			#sentence to the numpy array if the period for the 
			#sentence is contained on this line. Otherwise,
			#add last sentence to first sentence of next line 
			if iterator == len(sentences):
				if line.endswith('.'):
					sentence_array.append(sentence)
					last_sentence = ' '
				else:
					last_sentence = sentence
			else:
				sentence_array.append(sentence)
			iterator += 1	
	print sentence_array
	return sentence_array

if __name__ == '__main__':
	file_name = '~/Documents/Python_Files/Machine_Learning/National_Language_Profiler/test_file.txt'
	Txt_Parser(file_name)
		  
