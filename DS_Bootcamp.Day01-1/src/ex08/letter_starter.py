import sys

def latter_generator(email):
    file = open("employees.tsv", "r")
    data = set()
    for line in file:
        data.add(tuple(line.split("\t")))
    file.close()
    
    for lines in data:
        if lines[2].strip() == email:
            print(f"Dear {lines[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        latter_generator(sys.argv[1])