import os

def is_english(str):
    common_words = ['have','for','not','say','with','that','and','the']
    if any(word in str for word in common_words):
        return True
    return False

def decrypt(message):
    result = ''
    for letter in message:
        ascii_value = ord(letter)
        ascii_value = 158 - ascii_value
        letter = chr(ascii_value)
        result += letter
    return result


path = 'C:\\Users\\benja\\Desktop\\txt_files'

for filename in os.listdir(path):
    with open(os.path.join(path, filename),'r') as file:
        contents = file.read()
        if is_english(decrypt(contents)):
            print(filename + ' : ' + decrypt(contents))

print('done')
