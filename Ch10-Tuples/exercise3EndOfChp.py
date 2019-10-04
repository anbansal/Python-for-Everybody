import string


def countWords(fhand):
    count = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.translate(line.maketrans('', '', string.digits))
        line = line.translate(line.maketrans('', '', string.whitespace))
        line = line.lower()
        words = line.split()
        for word in words:
            for letter in word:
                count[letter] = count.get(letter, 0) + 1

    letters = list()
    countLetters = 0
    for key, value in list(count.items()):
        letters.append((value, key))
        countLetters += value
    letters.sort(reverse=True)
    for num, letter in letters:
        print(letter, num,100.0*num/countLetters)


def openFile():
    while True:
        fname = input("Type your file name: ")  # enter wordsFile.txt
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
    countWords(fhand)
    fhand.close()
