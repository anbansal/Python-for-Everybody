def parseString(str):
    stPos = str.find('@')
    if stPos < 0:
        return "No mailing server found"
    endPos = str.find(' ', stPos)
    if endPos < 0:
        endPos = len(str)
    return str[stPos + 1:endPos]


if __name__ == '__main__':
    mailAddress = input("Enter your mailing id: ")
    print("The mailing server is", parseString(mailAddress))
