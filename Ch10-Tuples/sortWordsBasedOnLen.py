import string


def sortWordsLen(str):
    words = str.split()
    t = list()
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    result = list()
    for length, word in t:
        result.append(word)
    return result


def getString():
    line = input("Type your sentence: ")
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    return line


if __name__ == '__main__':
    sentence = getString()
    print(sortWordsLen(sentence))
