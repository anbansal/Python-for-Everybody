import re


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


def useRe(fhand):
    for line in fhand:
        line = line.rstrip()
        if re.search('^From:.+@', line):
            print(line)


if __name__ == '__main__':
    fhand = openFile()
    useRe(fhand)
