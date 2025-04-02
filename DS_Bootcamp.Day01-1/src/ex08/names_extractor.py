import sys

def names_extractor(file_name):
    file = open(file_name, "r")
    email_adress = set()
    for line in file:
        email_adress.add((line.replace("\n", "")))
    file.close()

    output = open("employees.tsv", "w")
    output.write(f"Name\tSurname\tE-mail")
    for adress in email_adress:
        name, surname = (adress.split("@")[0]).split(".")

        name = name.capitalize()
        surname = surname.capitalize()

        output.write(f"\n{name}\t{surname}\t{adress}")
        
    output.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extractor(sys.argv[1])