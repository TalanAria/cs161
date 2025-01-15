x = 31
print(x, bin(x), hex(x))  # Printing x in decimal, binary, and hexadecimal

x = 18
print(x, bin(x), hex(x))  # Printing x in decimal, binary, and hexadecimal

# TypeError: 'float' object cannot be interpreted as an integer
# because it was a float

y = 0b1011  # Binary representation of 11
z = 0x90    # Hexadecimal representation of 144
print(y, z)  # Printing y and z

w = x + y + z  # Adding x, y, and z together

print(f"the sum is ,{w}")  # Printing the sum of x, y, and z


# Compression calculation
original_size = 240  # Original size of the text
dictionary_size = 25  # Size of the dictionary
compressed_text_size = 148  # Compressed text size

# Function to calculate and print the compression percentage
def percent_of_compression(original_size, dictionary_size, compressed_text_size):
    percent_of_compression = 1 - ((compressed_text_size + dictionary_size) / original_size)
    print(f"Compressed text size: {compressed_text_size} characters \n     Dictionary size: {dictionary_size} characters \n               Total: {compressed_text_size + dictionary_size}\n  Original text size: {original_size} \n         Compression: {percent_of_compression * 100}")  # Printing compression info

percent_of_compression(original_size, dictionary_size, compressed_text_size)  # Calling function with values

percent_of_compression(300, 50, 90)  # Calling function with different values


# Two’s complement function

def two_complment(number):
    if -127 <= number <= 127:
        number_str = str(number)
        if number_str[0] == "-":
            binary = format(number, '08b')
            counter = 0
            invert_binary = ""
            for characters in binary:
                if binary[counter] == "1":
                    invert_binary = invert_binary + "0"
                else:
                    invert_binary = invert_binary + "1"
                counter = counter + 1
            num1 = int(invert_binary, 2)
            sum = num1 + 1
            binary_sum = format(sum, '08b')
            print(binary_sum)
        else:
            print(format(number, '08b'))

two_complment(int(-23))  # Calling two_complment with a negative number
two_complment(int(44))  # Calling two_complment with a positive number
