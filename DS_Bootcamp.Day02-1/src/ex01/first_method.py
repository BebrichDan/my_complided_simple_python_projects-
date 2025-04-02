class Research:
    def file_reader():
         with open("../ex00/data.csv") as file:
            return (file.read())


if __name__ == '__main__':
    print(Research.file_reader())