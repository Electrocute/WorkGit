import filecmp
import os

from struct import *

original_file = input("Enter the file you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);
#file_size = input( "Enter the size of the file in bytes: ")

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

def writeBits(number, write_value):
    print("number to write: ", number, "with value of: ", write_value)
    bytes_to_write = number/8
    remainder = number%8
    print("remainder is: ", remainder)
    bytes_to_write = int(bytes_to_write)
    print("Bytes to write:  ", bytes_to_write)
    if bytes_to_write>0:
        for i in range(bytes_to_write):
            print("inside for loop in writeBits")
            if write_value == 0:
                new_file.write(b'\x00')
                print("writing 00")
            else:
                new_file.write(b'\xFF')
                print("writing FF")
        return(remainder)


def changeValue(newValue, remainder):
    print("changing value")
    print("the remainder is: ", remainder)
    if(remainder == 0):
        value = newValue
        print("changed value to", value)
        writeBits(int(n), int(value))
        return
    if remainder == 1:
        if newValue ==0 :
            
            new_file.write(change_1^0x00)
        else:
            new_file.write(change_1^0xFF)
    elif remainder == 2:
        if newValue ==0 :
            new_file.write(change_2^0x00)
        else:
            new_file.write(change_2^0xFF)
    elif remainder ==3:
        if newValue ==0 :
            new_file.write(change_3^0x00)
        else:
            new_file.write(change_3^0xFF)
    elif remainder == 4:
        if newValue ==0 :
            new_file.write(change_4^0x00)
        else:
            new_file.write(change_4^0xFF)
    elif remainder ==5:
        if newValue ==0 :
            new_file.write(change_5^0x00)
            print(change_5^0x00, "is the change byte")
        else:
            new_file.write(change_5^0xFF)
            print(change_5^0xFF, "is the change byte")
    elif remainder == 6:
        if newValue ==0 :
            new_file.write(change_6^0x00)
        else:
            new_file.write(change_6^0xFF)
    elif remainder ==7:
        if newValue ==0 :
            new_file.write(change_7^0x00)
        else:
            new_file.write(change_7^0xFF)
    
    value = newValue
    print("changed value to", value)
    to_write = int(n)-(8-int(remainder))
    remainder = writeBits(to_write)
    return(remainder)

#file_length_binary = file_size * 8

mask_1 = 0x80  # 0b1000
mask_2 = 0x40  # 0b0100
mask_3 = 0x20  # 0b0010 
mask_4 = 0x10  # 0b0001 
mask_5 = 0x08  # 0b1000
mask_6 = 0x04  # 0b0100
mask_7 = 0x02  # 0b0010 
mask_8 = 0x01  # 0b0001 

newValue = 0

def processByte(new_byte, remainder):
    if (new_byte > 0 ):
        newValue = 1
    else :
        newValue = 0 
    if newValue == value : 
        temp_remainder = remainder
        number_to_write = int(n) + int(temp_remainder)
        remainder = writeBits(number_to_write, value)
    else:
        remainder = changeValue(newValue, remainder)
    return(remainder)

number_to_write = 0

with open(original_file, "rb") as f:
    byte = f.read(1)
    while byte:
        print("Byte as read: ", byte)
        #new_byte = struct.unpack(byte)
        print("Byte unpacked: ", byte[0])

        new_byte = byte[0] & mask_1
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_2
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_3
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_4
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_5
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_6
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_7
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        new_byte = byte[0] & mask_8
        print("after mask: ", new_byte)
        remainder = processByte(new_byte, remainder)

        # Do stuff with byte.
        byte = f.read(1)




#new_file.tofile(final_product)
