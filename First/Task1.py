def string_itoBase(nb, base):
    if not  nb.isnumeric():
        return ("usage ")
    elif not base.isnumeric():
        return ("usage")

    b = ' '
    while nb > 0:
        b = str(nb % base) + b
        nb = nb // base
        return (b)


if __name__ == '__main__':
    # string_itoBase()
    print(string_itoBase(str(int(input())), str(int(input()))))
