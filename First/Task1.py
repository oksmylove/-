
def string_itoBase(nb, base):
    b = ' '
    while nb > 0:
        b = str(nb % base) + b
        nb = nb // base
    return(b)

if __name__ == '__main__':
#доделать функцию main, чтобы выводила usage

    print(string_itoBase(int(input()), int(input())))

