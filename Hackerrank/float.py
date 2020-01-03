import decimal

a = .1 + .2
print(a)
print('{0:.64f}'.format(a))

print(.1 + .2)
b = .1 + .2
c = float(decimal.Decimal('.1') + decimal.Decimal('.2'))
print(c)

print(.1)
print(.1 + .2)

print(.3 == .1 + .2)

