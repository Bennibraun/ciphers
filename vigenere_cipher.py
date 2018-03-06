import random
import os

with open('C:\\Users\\bbraun0361\\Desktop\\txt_files\\file_012499.txt','r') as file:
    contents = file.read()

keyword = ''

for i in range(0, 2249):
    keyword += 'vigenere'

Matrix = [[0 for x in range(92)] for y in range(92)]

x = 0
y = 0

for m in range(92):
    for i in range(92):
        Matrix[m][i] = chr() # don't know what to put in the chr() function... need to fill in table
        
print(Matrix)
