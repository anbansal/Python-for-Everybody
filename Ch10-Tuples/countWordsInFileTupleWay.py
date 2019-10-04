import string


def countWords(fhand):
    count = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1

    words = list()
    for key, value in list(count.items()):
        words.append((value, key))
    words.sort(reverse=True)
    for num, word in words[:15]:
        print(word, num)


def openFile():
    while True:
        fname = input("Type your file name: ")  # enter romeo_full.txt
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
