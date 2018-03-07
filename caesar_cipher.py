def shift(letter, n):
    ascii_code = ord(letter)
    while ascii_code + n < 32:
        ascii_code += 95
    return chr(ascii_code + n)

def encrypt(message, shift_amount):
    result = ''

    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    result = ''

    for letter in message:
        result += shift(letter, -(shift_amount))

    return result

with open('C:\\Users\\benja\\Desktop\\txt_files\\file_001597.txt','r') as file:
    contents = file.read()

common_words = ['and','they','are','is','can','find','found','cipher','text','message']

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

for i in range(0, 50):
     decr_mess = decrypt(contents, i)
     print(decr_mess)
    
