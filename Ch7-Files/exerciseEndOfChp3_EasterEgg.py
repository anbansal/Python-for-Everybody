def checkFile(fhand):
    count = 0
    str = "Subject:"
    for line in fhand:
        if line.find(str) != -1:
            count = count + 1

    print("The total no of lines which start with", str, "are ", count)


def openFile():
    while True:
        fname = input("Type your file name: ")
        try:
            fhand = open(fname)
            break
        except:
            print("File cannot be opened:", fname)
            if fname.strip() == "na na boo boo":
                print("NA NA BOO BOO TO YOU - You have been punk'd!")
            print("Please try again!")
            continue

    return fhand


if __name__ == '__main__':
    fhand = openFile()
    checkFile(fhand)
    fhand.close()
