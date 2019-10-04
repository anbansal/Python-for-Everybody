def checkWord(dictionary, word):
    return word in dictionary


def fileToStrings(fhand):
    wordsToString = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            wordsToString[word] = ''
    return wordsToString


def openFile():
    while True:
        fname = input("Type your file name: ") #enter words.txt
        fname = fname.strip()
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
    dictionary = fileToStrings(fhand)
    word = input("Type word to be searched: ")
    print("Result: ", checkWord(dictionary, word))
    fhand.close()
