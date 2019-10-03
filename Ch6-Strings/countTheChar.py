def countChar(str, chr):
    count = 0
    str = str.upper()
    chr = chr.upper()
    for char in str:
        if chr == char:
            count = count + 1

    return count


if __name__ == '__main__':
    str = input("Type your word: ")
    char = input("Type your character: ")
    print(char, "appears", countChar(str, char), "times in the", str)
