def read_and_write(input_file, output_file):
    input = open(input_file, "r")
    output = open(output_file, "w")
    for line in input:
        str = line.replace(",", "\t")
        output.write(str)
    input.close()
    output.close()

if __name__ == '__main__':
    read_and_write("ds.csv", "ds.tsv")
