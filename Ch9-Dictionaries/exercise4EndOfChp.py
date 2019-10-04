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


def largestValueInDict(dictionary):
    largest = None
    returnKey = None
    for item in dictionary:
        try:
            if largest is None or dictionary[item] > largest:
                largest = dictionary[item]
                returnKey = item
        except:
            pass
    return {returnKey: largest}


def smallestValueInDict(dictionary):
    smallest = None
    returnKey = None
    for item in dictionary:
        try:
            if smallest is None or dictionary[item] < smallest:
                smallest = dictionary[item]
                returnKey = item
        except:
            pass
    return {returnKey: smallest}


if __name__ == '__main__':
    fhand = openFile()
    categ = countSenders(fhand)
    print("The largest value is: ")
    printDict(largestValueInDict(categ))
    print("The smallest value is: ")
    printDict(smallestValueInDict(categ))
    fhand.close()
