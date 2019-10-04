def writeOnFile(fhand):
    fname = input("Type the name of existing file to be copied: ")
    try:
        fhandR = open(fname,'r')
    except:
        print("The file",fname,"does not exist in current folder")
        exit()
    for line in fhandR:
        fhand.write(line)
    fhandR.close()
    print("done!")


if __name__ == '__main__':
    fname = input("Type the name of file where you want the data to be copied: ")
    fhand = open(fname,'a')
    writeOnFile(fhand)
    fhand.close()
