
inputfile = "script.txt"

myfile = open(inputfile, mode="r", encoding="latin_1")

#print(myfile.read())

what_to_look = '<font face=verdana color="#000000"'
#what_to_look = "meta"

print(what_to_look)
count = 0

for line in myfile:
    if what_to_look in line:
        endJpg = line.find("JPG")
        #print(endJpg)
        image = line[57:endJpg+3]
        #print(line)
        print(image.strip())

