import filecmp
import os
from bitstring import BitArray, BitStream

original_file = input("Enter the file you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
int n 
n = input("Rate of oversampling: ")

old_file = open(original_file, 'rb');
new_file = open(final_product, 'wb');

file_statistics = os.stat('old_file')
file_length = file_statistics.st_size
file_length_binary = file_length * 7

old_file_binary = Bits(old_file)
new_file_binary = Bits(new_file)
i=0
bool temp
while(j<file_length_binary)
	temp = old_file_binary.read(j) 
	if temp = 1
		for(k=0, k<n, k++)
			new_file_binary.append(0b1)
	else
		for(k=0, k<n, k++)
			new_file_binary.append(0b0)