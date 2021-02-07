def string_comparison(a: str, b: str):
    if b.find('*') != -1:
        for i in range(b.find('*')):
            if a[i] != b[i]:
                return 'KO'
        return 'OK'
    else:
        if a == b:
            return 'OK'
        else:
            return 'KO'
if __name__ == '__main__':

    print(string_comparison(str(input()),
                            str(input())))
