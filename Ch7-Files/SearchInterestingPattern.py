def search(str):
    count = 0
    fhand = open('mbox-short.txt')
    # content = fhand.read()
    for line in fhand:
        if line.find(str) != -1:
            print(line.rstrip())
            count = count + 1

    print("The total no of lines which start with", str, "are ", count)


if __name__ == '__main__':
    str = input("Type your search pattern: ")  # str = @uct.ac.za;str = From:
    search(str)
