#Chris, Katie, Eleni
#CS151
#lab10
#12/2/21

# A function load_morse_dictionary which loads the data from the file morsecode.txt, builds a dictionary
# (mapping morse code to letters, numbers, and punctuation), and returns it.

import string

def load_morse_dictionary():
	morse_dictionary = {}
	try:
		file = open("morsecode.txt", "r")
		for line in file:
			(val, key) = line.split(	)
			morse_dictionary[key] = val

	except FileNotFoundError:
		print("Invalid filename")

	file.close()
	return morse_dictionary

# A function decode_file which, given the morse dictionary and a filename containing morse code lines,
# decodes the contents of the file to the console.

def decode_file(dictionary, morse_file):
	file = open(morse_file)
	for line in file:
		codes = line.split( )
		for code in codes:
			print(dictionary[code], end="")

def main():
	decode_file(load_morse_dictionary(), input("Enter the filename: "))

main()