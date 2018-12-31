
inputfile = "C:\Learning\PythonLearning\Most-Popular-Letter-Passes.txt"

myfile = open(inputfile, mode="r", encoding="latin_1")

#print(myfile.read())

for num, line in enumerate(myfile, 1):
    print(str(num) + " " + line.strip())