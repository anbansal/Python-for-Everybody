def chop(newList):
    print("Doing Chop()")
    try:
        del newList[0]
        newList.pop()
    except:
        pass


def middle(newList):
    print("Doing middle()")
    try:
        return newList[1:len(newList) - 1]
    except:
        return None


def getList():
    newList = []
    print("This program let you enter the values of the list\nType 'done' when you are done!!!")
    while True:
        str = input("Enter a value: ")
        if str.lower().strip() == "done":
            break
        newList.append(str)
    return newList


if __name__ == '__main__':
    newList = getList()
    origList = newList[:]
    print("The list you entered is :\n", origList)
    chop(newList)
    print("The list you entered is :\n", origList)
    print("The list came from chop() is :\n", newList)
    mdList = middle(origList)
    print("The list you entered is :\n", origList)
    print("The list came from middle() is :\n", mdList)
