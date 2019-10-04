def search(fhand,str):
    count = 0
    for line in fhand:
        if line.find(str) != -1:
            print(line.rstrip())
            count = count + 1

    print("The total no of lines which start with", str, "are ", count)


if __name__ == '__main__':
    while True:
        fname = input("Type your file name: ")
        try:
            fhand = open(fname)
            str = input("Type your search pattern: ")  # str = @uct.ac.za;str = From:
            break
        except:
            print("Could not open the file", fname)
            exit()

    search(fhand,str)
