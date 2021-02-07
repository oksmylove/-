
def string_itoBase():
    nb=str(input())
    nb=str(nb)
    if not nb.isdigit():
        print("Usage")
        #nb=int(nb)
    base=str(input())
    base=str(base)
    if not base.isdigit():
        print("Usage")
        #base=int(base)
    else:    
        b = ''
        nb=int(nb)
        base=int(base)
        while nb > 0:
            b = str(nb % base) + b
            nb = nb // base
    return(b)
string_itoBase()


