import filecmp

original_file = input("Enter the file you wish to over sample: ");
print("the file you want to oversample is:", original_file);
final_product = input("Enter the oversampled file: ");
print("The oversampled product of ", original_file, " is stored in ", final_product);


old_file = open(original_file, 'r');

new_file = open(final_product, 'w');

old_file.read()
