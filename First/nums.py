nb = int(input())
base = int(input())

b = ''
while nb > 0:
    b = str(nb % base) + b
    nb = nb // base

print(b)
