if __name__ == '__main__':
    s = input()
    b1 = False
    b2 = False
    b3 = False
    b4 = False
    b5 = False
       
    for char in s:
        if(not b1):
            b1 = char.isalnum()
        if(not b2):
            b2 = char.isalpha()
        if(not b3):
            b3 = char.isdigit()
        if(not b4):
            b4 = char.islower()
        if(not b5):
            b5 = char.isupper()
        
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
