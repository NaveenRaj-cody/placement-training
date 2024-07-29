if __name__ == '__main__':
    s = input()
    an = 0
    ap = 0
    d = 0
    l = 0
    u = 0
    for i in range(len(s)):
        if s[i].isalnum():
            an += 1
        if s[i].isalpha():
            ap += 1
        if s[i].isdigit():
            d += 1
        if s[i].islower():
            l += 1
        if s[i].isupper():
            u += 1   
    if an > 0:
        print(True)
    else:
        print(False)       
    if ap > 0:
        print(True)
    else:
        print(False)       
    if d > 0:
        print(True)
    else:
        print(False)      
    if l > 0:
        print(True)
    else:
        print(False)     
    if u > 0:
        print(True)
    else:
        print(False)
