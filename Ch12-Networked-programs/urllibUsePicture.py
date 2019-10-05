import urllib.request


def useUrllib(address):
    img = urllib.request.urlopen(address)
    fhand = open('cover3.jpg', "wb")
    count = 0
    while True:
        imgData = img.read(102400)
        if len(imgData) < 1: break
        count += len(imgData)
        fhand.write(imgData)
    print("Copied", count, " amount of data from", address)


if __name__ == '__main__':
    address = 'http://data.pr4e.org/cover3.jpg'
    useUrllib(address)
