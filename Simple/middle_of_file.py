# Find middle of file
import random
import string
import os

def creation_random_file():
    f = open('numbers_str.txt', 'w+')
    for i in range(259):
        letters = string.ascii_lowercase
        str = ''.join(random.choice(letters) for i in range(10))
        f.write(str)
    f.close()

creation_random_file()
f = open('numbers_str.txt', 'r')
#print(len(f.readline())) # count of strings
#size = os.stat('numbers_str.txt').st_size
#sizekb = os.path.get('numbers_str.txt')
#print(size)
#print(sizekb)

text = f.read()
print(len(text))