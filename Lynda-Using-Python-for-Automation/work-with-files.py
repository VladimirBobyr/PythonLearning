'''f = open('Exercise Files\inputFile.txt','r')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)
f.close()
'''
file_read = open('Exercise Files\inputFile.txt','r')
file_write_passed = open('passfile.txt', 'w')
file_write_failed = open('failfile.txt', 'w')
for line in file_read:
    line_split = line.split()
    if line_split[2] == 'P':
        file_write_passed.write(line)
    else:
        file_write_failed.write(line)
file_read.close()
file_write_passed.close()
file_write_failed
