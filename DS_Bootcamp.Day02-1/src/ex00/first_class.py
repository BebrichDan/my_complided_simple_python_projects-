class Must_read:
    file = open("data.csv")

    for string in file:
        print(f"{string.strip()}")

    file.close()

if __name__ == '__main__':
    Must_read()