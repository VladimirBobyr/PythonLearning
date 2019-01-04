import sys

filename = 'Lessons_List.txt'

try:
    print('Inside TRY')
    myfile = open(filename, mode='r', encoding='latin_1')
except Exception:
    print('Inside TRY')
    print('Error Found!')
    sys.exit()
else:
    print('Inside ELSE')
    print(myfile.read())
finally:
    print('Inside FINALY')


print('=============== EOF =================')