def uniqueWordsList(fhand):
    uniqueWords = list()
    for line in fhand:
        words = line.split()
        for word in words:
            try:
                uniqueWords.remove(word)
            except:
                pass
            uniqueWords.append(word)
    uniqueWords.sort()
    return uniqueWords


def openFile():
    while True:
        fname = input("Type your file name: ")
        try:
            fhand = open(fname)
            break
        except:
            print("Could not open the file", fname)
            print("Please try again!")
            continue

    return fhand


if __name__ == '__main__':
    fhand = openFile()
    words = uniqueWordsList(fhand)
    print(words)
    fhand.close()
