def countNumber():
    prompt = "Enter a number: "
    count = 0
    total = 0
    while True:
        line = input(prompt)
        if line == "done" or line == "Done" or line == "DONE":
            break
        try:
            num = float(line)
        except:
            print("Invalid input")
            continue
        count = count + 1
        total = total + num
    if count != 0:
        print("Total: ", total)
        print("Count: ", count)
        print("Average: ", total / count)
    else:
        print("Nothing valuable entered!")


if __name__ == '__main__':
    countNumber()
