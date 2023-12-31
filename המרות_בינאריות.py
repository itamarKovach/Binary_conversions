def decimal_to_binary(decimal, num_bits):
    binary = bin(decimal)[2:].zfill(num_bits)
    return binary

def invert_and_add_one(binary):
     if binary == '0' * len(binary):
        return '0' * (len(binary))

     inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    
     result = bin(int(inverted, 2) + 1)[2:].zfill(len(binary))
     return result
decimal = int(input("enter a decimal number: "))
num_bits = int(input("enter number of bits: "))

binary = decimal_to_binary(decimal, num_bits)
result = invert_and_add_one(binary)

print("the binary value of negative " + str(decimal) + " is: " + result)
