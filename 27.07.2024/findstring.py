def count_substring(string, sub_string):
    number = 0
    i = 0
    while True:
        try:
            i = string.index(sub_string, i) + 1
            number += 1
        except ValueError:
            break
    return(number)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
