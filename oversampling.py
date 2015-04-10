import filecmp
import os
from bitstring import Bits, BitStream, BitArray

original_file = input("Enter the file with path you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file with path: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
#file_size = input( "Enter the size of the file in bytes: ")
n = 0
n = input("Rate of oversampling: ")


mask_1 = 0x8  # 0b1000
mask_2 = 0x4  # 0b0100
mask_3 = 0x2  # 0b0010 
mask_4 = 0x1  # 0b0001 
remainder = 0
value = 0

old_file = open(original_file, 'wb');
new_file = open(final_product, 'wb');

def writeBits
	number = n+remainder
	bytes_to_write = number/4
	remainder = number%4
	if value == 1:
		new_file.write(0xF)
	else:
		new_file.write(0x0)
	return

def changeValue
#file_length_binary = file_size * 8

mask_1 = 0b1000
mask_2 = 0b0100
mask_3 = 0b0010 
mask_4 = 0b0001 
remainder = 0
value = 0
with open(original_file, "rb") as f:
    byte = f.read(1)
    while byte:
    	new_byte = byte && mask_1
    	if (new_byte > 0 ):
    		newValue = 1
    	else :
    		newValue = 0
    	if newValue == value : 
    		writeBits()
    	else:
    		changeValue()

        # Do stuff with byte.
        byte = f.read(1)




new_file_binary.tofile(new_file)