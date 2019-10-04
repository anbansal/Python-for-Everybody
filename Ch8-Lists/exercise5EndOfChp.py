def countFrom(fhand):
    count = 0
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'): continue
            try:
                print((line.split())[1])
            except:
                continue
            count = count + 1
    print("There were", count, "lines in the file with From as the first word")


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


if __name__ == '__main__':
    fhand = openFile()
    countFrom(fhand)
