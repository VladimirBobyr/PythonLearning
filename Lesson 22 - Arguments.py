import sys
import os

print("Hello!")

print(sys.argv)
print(sys.argv[1:])

# ========== Check whether is arguments ============ #

x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this program is python.exe script with arguments or w/t arguments")
    print("Argements: " + str(sys.argv[1:]))
else:
    print("Arguments were not provided")

os.system("dir")
#os.mkdir("mydir")
sys.exit(2)