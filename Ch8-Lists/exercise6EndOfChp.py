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
    try:
        print("Maximum:", max(number))
        print("Minimum:", min(number))
    except:
        print("You did not entered any number !!!")
