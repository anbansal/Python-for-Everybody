def copyTillDone():
    while True:
        line = input('>')
        if line == "done" or line == "Done" or line == "DONE":
            break
        else:
            print(line)

    print("done")


if __name__ == '__main__':
    copyTillDone()
