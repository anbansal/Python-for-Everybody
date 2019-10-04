def countSenders(fhand):
    count = dict()
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'): continue
            try:
                senderId = (line.split())[1]
                count[senderId] = count.get(senderId, 0) + 1
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


def minMaxValueInDict(dictionary):
    lst = list()
    for key, value in list(dictionary.items()):
        lst.append((value, key))
    lst.sort(reverse=True)
    print("The largest value is: ")
    print(lst[0][1], lst[0][0])
    print("The smallest value is: ")
    print(lst[len(lst) - 1][1], lst[len(lst) - 1][0])


if __name__ == '__main__':
    fhand = openFile()
    categ = countSenders(fhand)
    minMaxValueInDict(categ)
    fhand.close()
