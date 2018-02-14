import random

def random_chars():
    result = ''
    for i in range(32,127):
        result += chr(i)
    return ''.join(random.sample(result,len(result)))

alphabet = random_chars()
key = random_chars()

def encrypt(message):
    loc = 0
    result = ''

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    loc = 0
    result = ''

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result

unencrypted_message = "This is a substitution cipher. #*$^#({}|_+><>`kfsdalfjiasf793240"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)