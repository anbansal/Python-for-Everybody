def countTimeHour(fhand):
    count = dict()
    for line in fhand:
        if line.startswith('From'):
            if line.startswith('From:'): continue
            try:
                time = (line.split())[5]
                hour = (time.split(':'))[0]
                count[hour] = count.get(hour, 0) + 1
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


def sortDictionary(dictionary):
    lst = list()
    for key, value in list(dictionary.items()):
        lst.append((key, value))
    lst.sort(reverse=False)
    return lst


def printDict(dictionary):
    lst = sortDictionary(dictionary)
    for key, value in lst:
        print(key, value)


def minMaxValueInDict(dictionary):
    lst = sortDictionary(dictionary)
    print("The largest value is: ")
    print(lst[0][1], lst[0][0])
    print("The smallest value is: ")
    print(lst[len(lst) - 1][1], lst[len(lst) - 1][0])


if __name__ == '__main__':
    fhand = openFile()
    categ = countTimeHour(fhand)
    printDict(categ)
    fhand.close()
