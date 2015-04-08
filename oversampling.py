import filecmp
import os
from bitstring import Bits, BitStream, BitArray

original_file = input("Enter the file with path you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file with path: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
file_size = input( "Enter the size of the file in bytes: ")
n = 0
n = input("Rate of oversampling: ")

old_file = open(original_file, 'wb');
new_file = open(final_product, 'wb');


file_length_binary = file_size * 8

old_file_binary_read = Bits(old_file)
new_file_binary_read = Bits(new_file)

old_file_binary = BitArray(old_file_binary_read)
new_file_binary = BitArray(new_file_binary_read)

i=0
j=0
new_file_placekeeper = 0
for j in range(file_length_binary) :
	temp = old_file_binary(j) 
	if temp == 1:
		for x in  range(n):
			new_file_binary.insert(0b1, (new_file_placekeeper))
			new_file_placekeeper = new_file_placekeeper + 1
	else:
		for x in range(n):
			new_file_binary.insert(0b0, new_file_placekeeper)
			new_file_placekeeper = new_file_placekeeper + 1

new_file.write(new_file_binary)