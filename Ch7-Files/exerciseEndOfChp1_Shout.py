def shout(fhand):
    for line in fhand:
        print(line.upper())


if __name__ == '__main__':
    while True:
        fname = input("Type your file name: ")
        try:
            fhand = open(fname)
            break
        except:
            print("Could not open the file", fname)
            print("Please try again!")
            continue

    shout(fhand)
    print("Done!")
    fhand.close()
