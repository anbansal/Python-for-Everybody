def categorize(fhand):
    count = dict()
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'): continue
            try:
                weekday = (line.split())[2]
                count[weekday] = count.get(weekday, 0) + 1
            except:
                continue
    return count


def openFile():
    while True:
        fname = input("Type your file name: ")  # enter mbox-short.txt
        fname = fname.strip()
        try:
            fhand = open(fname)
            break
        except:
            print("Could not open the file", fname)
            print("Please try again!")
            continue

    return fhand


def printDict(dictionary):
    words = list(dictionary.keys())
    words.sort()
    for key in words:
        print(key, dictionary[key])


if __name__ == '__main__':
    fhand = openFile()
    categ = categorize(fhand)
    printDict(categ)
    fhand.close()
