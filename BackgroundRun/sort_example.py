list1 = ['test=1','test=2','test=3']

print(sorted(list1, key=str.split('=')(1)))