def countLetters(str):
    count = dict()
    for c in str:
        c = c.lower()
        if c == ' ':continue
        count[c] = count.get(c, 0) + 1
    return count


def getWord():
    str = input("Type your word: ")
    return str


if __name__ == '__main__':
    word = getWord()
    count = countLetters(word)
    print(count)
