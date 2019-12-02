from random import random

def creation_random_file():
    f = open('numbers.txt', 'w+')
    for i in range(10000):
        f.write(str(random() * 1000) + '\n')
    f.close()

creation_random_file()