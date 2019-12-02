import math

def sqroot(x):
    return math.sqrt(x)

y = sqroot(2)
print(y)
sqroot_lambda = lambda x: math.sqrt(x)

print(sqroot_lambda(2))