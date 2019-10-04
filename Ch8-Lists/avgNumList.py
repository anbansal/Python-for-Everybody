def avgNumList(listNumber):
    try:
        average = sum(listNumber)/len(listNumber)
    except:
        average = "No value entered !!!"
    print("Average:", average)


def getNum():
    number = []
    while True:
        str = input("Enter a number: ")
        try:
            if str.lower().strip() == "done":
                break
            num = float(str)
        except:
            print("%s is not a number!" % str)
            print("Please try again!")
            continue
        number.append(num)

    return number


if __name__ == '__main__':
    number = getNum()
    avgNumList(number)
