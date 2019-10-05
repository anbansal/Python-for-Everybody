import re


def useRe(fhand, str):
    total = 0
    count = 0
    for line in fhand:
        line = line.rstrip()
        x = re.findall(str, line)
        if len(x) > 0:
            total += float(x[0])
            count += 1
    return total / count


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
    str = 'New Re.*: ([0-9.]+)'
    value = useRe(fhand, str)
    print(int(value))
