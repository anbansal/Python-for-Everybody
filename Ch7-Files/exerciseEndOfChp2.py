def countValue(fhand):
    count = 0
    value = 0
    for line in fhand:
        if line.find('X-DSPAM-Confidence:') != -1:
            atpos = line.find(':')
            floatValue = float(line[atpos + 1:])
            value = value + floatValue
            count = count + 1
    avgSpamVal = value / count
    print("Average spam confidence:", avgSpamVal)


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
    countValue(fhand)
    fhand.close()
