import re


def useRe(fhand, str):
    count = 0
    for line in fhand:
        line = line.rstrip()
        x = re.findall(str, line)
        if len(x) > 0:
            count += 1
    return count


def getStr():
    str = input("Enter a regular expression: ")
    return str


if __name__ == '__main__':
    # fname = "mbox-short.txt"
    fname = "mbox.txt"
    try:
        fhand = open(fname)
    except:
        print("The file",fname,"does not exist!!!\nExiting....")
        quit()
    str = getStr()
    count = useRe(fhand, str)
    print(fname, "had", count, "lines that matched", str)
