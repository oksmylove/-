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

    print(string_comparison('aaaaa', 'aa*'))
    print(string_comparison('aaaaa', 'a********'))
    print(string_comparison('aaaaa', 'b***aaa'))
    print(string_comparison('aaaaa', ''))
    print(string_comparison('aaaaa', 'aaaaa'))
    print(string_comparison('aaaaa', 'aaaa'))
    print(string_comparison('aaaaa', 'daf'))
    print(string_comparison('aaaaa', '****'))
