import re
text = 'abcdfghijk'

parser = re.search('a[b-f]*f', text)
print(parser.group()) # 'abcdf'

parser = re.match('xb{1,4}z', text)
print(parser)
#print(parser.group()) # 'abcdf'
