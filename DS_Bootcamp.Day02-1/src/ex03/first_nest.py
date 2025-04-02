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
                    header = lines[0].strip().split(",")
                    if not all(part.isalpha() for part in header):
                        raise ValueError("Error: Invalid header format.")

                data = []
                strart_index_enume =  0 if not has_header else 1
                for index, line in enumerate(lines[strart_index_enume:]): 
                    values = line.strip().split(",")

                    if len(values) != 2:
                        raise ValueError(f"Error: Incorrect data format.")

                    if not all(v in {"0", "1"} for v in values):
                        raise ValueError(f"Error: Value in line is not corrrect {index}.")
                    
                    data.append([int(val) for val in values])

                return data

        except Exception as e:
            print(f"{e}")
            sys.exit(1)

        with open(self.file_path) as file:
            return file.read()
    
    class  Calculations:
        def counts(file_reader_return_list):
            eagles, tails = 0, 0
            for lines in file_reader_return_list:
                if lines[0] == 1:
                    eagles+=1
                else:
                    tails+=1
            return eagles, tails
            
        def fractions(eagles, tails):
            sum = eagles + tails
            number_percent_eagles = (eagles/sum)*100
            number_percent_tails = (tails/sum)*100
            return number_percent_eagles, number_percent_tails

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Error: You must provide a file path as an argument.")
        sys.exit(1)

    file_path = sys.argv[1]  
    research = Research(file_path)
    return_list = research.file_reader()
    print(return_list)
    eagles, tails = research.Calculations.counts(return_list)
    print(eagles, tails)
    persent1, persent2 = research.Calculations.fractions(eagles, tails)
    print(persent1, persent2)
