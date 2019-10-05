import urllib.request


def useUrllib(address):
    try:
        fhand = urllib.request.urlopen(address)
    except:
        exit(0)
    count = 0
    for line in fhand:
        str = line.decode().strip()
        count += len(str)
        if count < 3000:
            print(str)
    print("\nCopied data: ",count)


if __name__ == '__main__':
    address = input("Enter: ")
    useUrllib(address)
