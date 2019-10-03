def copyTillDone():
    while True:
        line = input('>')
        if line == "done" or line == "Done" or line == "DONE":
            break
        elif line[0] == '#':
            continue
        else:
            print(line)

    print("done")


if __name__ == '__main__':
    copyTillDone()
