# Learn for working with file in python
from random import random

def creation_random_file():
    f = open('numbers.txt', 'w+')
    for i in range(100):
        f.write(str(random() * 1000) + '\n')
    f.close()

creation_random_file()

f1 = open('numbers.txt', 'r')
f2 = open('numbers1.txt', 'w+')

list1 = []
for l in open('numbers.txt', 'r'):
    list1.append(float(l))
list1.sort()
print(list1)

for l in list1:
    f2.write(str(l)+'\n')

f1.close()
f2.close()
