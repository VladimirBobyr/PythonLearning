import re

# Usefule site for regular expression
#
# [\w.-]+    = Any letter .(point) or -(minus) - many

datafile = "dataset.xml"
inputfile = open(datafile, mode='r', encoding='latin_1')
resultsfile = open("results.txt", mode='w', encoding='latin_1')

# ====== Find all emails ===================== #
lookfor = r"[\w.-]+@[\w]+\.[\w.]+"
#lookfor = r"[\w.-]+@(?!intel\.com)[\w]+\.[\w.]+"   = in email exclude all intel.com

mytext = inputfile.read()

results = re.findall(lookfor, mytext)
for result in results:
    resultsfile.write(result + '\n')
    print(result)
print(len(results))

