import sys, os 

class Research:
    def __init__(self, file_path):
        if not file_path:
            raise ValueError("Error: File path is not spicified")
        
        if not os.path.exists(file_path):
            raise ValueError("Error: File not found or not exists")

        self.file_path = file_path

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path) as file:
                lines = file.readlines()

                if len(lines) < 2:
                    raise ValueError("Error: The file is too short.")
                
                if has_header:
                    header = lines[0].split(",")
                    if not all(part.isalpha() for part in header):
                        raise ValueError("Error: Invalid header format.")

                data = []
                for line in lines[1:]:
                    values = line.strip().split(",")

                    if len(values) != 2:
                        raise ValueError(f"Error: Incorrect data format.")

                    if not all(v in {"0", "1"} for v in values):
                        raise ValueError(f"Error: Value in line is not corrrect.")
                    
                    data.append([int(val) for val in values])

                return header, data

        except Exception as e:
            print(f"{e}")
            sys.exit(1)

        with open(self.file_path) as file:
            return file.read()
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: You must provide a file path as an argument.")
        sys.exit(1)

    file_path = sys.argv[1]  
    research = Research(file_path)
    print(research.file_reader())  