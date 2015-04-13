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


mask_1 = 0b1000
mask_2 = 0b0100
mask_3 = 0b0010 
mask_4 = 0b0001 
change_1 = 0b1000
change_2 = 0b1100
change_3 = 0b1110

remainder = 0
value = 0

old_file = open(original_file, 'wb');
new_file = open(final_product, 'wb');

def writeBits(number):
    
    bytes_to_write = number/4
    remainder = number%4
    if value == 1:
        new_file.write(0xF)
    else:
        new_file.write(0x0)
    return


def changeValue():
    if newValue == 0 :
        if remainder == 1:
            new_file.write(change_1^0x0)
        elif remainder == 2:
            new_file.write(change_2^0x0)
        elif remainder ==3:
            new_file.write(change_3^0x0)
    else :
        if remainder == 1:
            new_file.write(change_1^0xF)
        elif remainder == 2:
            new_file.write(change_1^0xF)
        elif remainder ==3:
            new_file.write(change_1^0xF)
    value = newValue
    writeBits(n-(4-remainder))

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
        new_byte = byte & mask_1
        if (new_byte > 0 ):
            newValue = 1
        else :
            newValue = 0
        if newValue == value : 
            number_to_write = n+remainder
            writeBits(number_to_write)
        else:
            changeValue()

        # Do stuff with byte.
        byte = f.read(1)




#new_file_binary.tofile(new_file)