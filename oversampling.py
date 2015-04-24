import filecmp
import os
from bitstring import Bits, BitStream, BitArray

from struct import *

original_file = input("Enter the file you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
#file_size = input( "Enter the size of the file in bytes: ")
n = 0
n = input("Rate of oversampling: ")


mask_1 = 0b10000000
mask_2 = 0b01000000
mask_3 = 0b00100000
mask_4 = 0b00010000
change_1 = 0b10000000
change_2 = 0b11000000
change_3 = 0b11100000
change_4 = 0b11110000
change_5 = 0b11111000
change_6 = 0b11111100
change_7 = 0b11111110

remainder = 0
value = 0

#old_file = open(original_file, 'rb');
new_file = open(final_product, 'wb');

def writeBits(number):
    
    bytes_to_write = number/8
    remainder = number%8
    if bytes_to_write>1:
        i = 1
        for i in range(bytes_to_write):
            if value == 1:
                new_file.write(0xFF)
            else:
                new_file.write(0x00)
            return


def changeValue():
    if remainder == 1:
        if newValue ==0 :
            new_file.write(change_1^0x0)
        else:
            new_file.write(change_1^0xF)
    elif remainder == 2:
        if newValue ==0 :
            new_file.write(change_2^0x0)
        else:
            new_file.write(change_20xF)
    elif remainder ==3:
        if newValue ==0 :
            new_file.write(change_3^0x0)
        else:
            new_file.write(change_3^0xF)
    elif remainder == 4:
        if newValue ==0 :
            new_file.write(change_4^0x0)
        else:
            new_file.write(change_4^0xF)
    elif remainder ==5:
        if newValue ==0 :
            new_file.write(change_5^0x0)
        else:
            new_file.write(change_5^0xF)
    elif remainder == 6:
        if newValue ==0 :
            new_file.write(change_6^0x0)
        else:
            new_file.write(change_6^0xF)
    elif remainder ==7:
        if newValue ==0 :
            new_file.write(change_7^0x0)
        else:
            new_file.write(change_7^0xF)
    
    value = newValue
    writeBits(n-(4-remainder))

#file_length_binary = file_size * 8

mask_1 = 0x80  # 0b1000
mask_2 = 0x40  # 0b0100
mask_3 = 0x20  # 0b0010 
mask_4 = 0x10  # 0b0001 
remainder = 0
value = 0
with open(original_file, "rb") as f:
    byte = f.read(1)
    while byte:
        print("Byte as read: ", byte)
        #new_byte = struct.unpack(byte)
        print("Byte unpacked: ", byte[0])
        new_byte = byte[0] & mask_1
        print("after mask: ", new_byte)
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




#new_file.tofile(final_product)