def largest(items):
    largest = None
    for item in items:
        if largest is None or item < largest:
            largest = item
    print("The largest item is", largest)


if __name__ == '__main__':
    #list = [3, 41, 34, 56, 89, -1.0]
    list = ["Adam","Evelyn","Jacob","Aysha"]
    largest(list)
