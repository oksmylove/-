nb = int(input())

b = ''
while nb > 0:
    b = str(nb % 2) + b
    nb = nb // 2

print(b)
