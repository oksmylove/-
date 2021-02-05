nb = int(input())
base = int(input())

b = ''
while nb > 0:
    b = str(nb % base) + b
    nb = nb // base
if nb>0:
    print('Ку-кин дза-дза')
print(b)
