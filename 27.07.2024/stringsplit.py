def split_and_join(line):
    words = line.split(" ")  # Split the string into a list of words
    hyphenated_string = "-".join(words)  # Join the words using a hyphen
    return hyphenated_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
