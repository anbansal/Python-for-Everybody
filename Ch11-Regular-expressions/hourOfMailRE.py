import re


def useRe(fhand):
    lst = list()
    total = 0
    for line in fhand:
        line = line.rstrip()
        x = re.findall('^From.* ([0-9][0-9]):', line)
        if len(x) > 0:
            # total += float(x[0])
            lst.append(x)
    # print(total/len(lst))
    print(lst)




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


if __name__ == '__main__':
    fhand = openFile()
    useRe(fhand)
