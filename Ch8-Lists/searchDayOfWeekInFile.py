def searchFunc(fhand):
    for line in fhand:
        if line.startswith('From'):
            line = line.rstrip()
            words = line.split()
            try:
                print(words[2])
            except:
                pass


def openFile():
    while True:
        fname = input("Type your file name: ")  # enter mbox-short.txt
        fname = fname.strip()
        try:
            fhand = open(fname)
            break
        except:
            print("File cannot be opened:", fname)
            print("Please try again!")
            continue

    return fhand


if __name__ == '__main__':
    fhand = openFile()
    searchFunc(fhand)
    fhand.close()
