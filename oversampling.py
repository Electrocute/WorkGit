import filecmp
import os
from bitstring import Bits, BitStream

original_file = input("Enter the file you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
n = 0
n = input("Rate of oversampling: ")

old_file = open(original_file, 'rb');
new_file = open(final_product, 'wb');

file_statistics = os.stat(original_file)
file_length = file_statistics.st_size
file_length_binary = file_length * 8

old_file_binary = BitStream(old_file)
new_file_binary = BitStream(new_file)
i=0

while j<file_length_binary :
	temp = old_file_binary.read(j) 
	if temp == 1:
		for x in  range(n):
			new_file_binary.append(0b1)
	else:
		for x in range(n):
			new_file_binary.append(0b0)