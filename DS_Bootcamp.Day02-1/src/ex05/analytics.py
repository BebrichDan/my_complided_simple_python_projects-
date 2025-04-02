import os
from random import randint

class Research:
    
    def __init__(self, file_path):
        if not file_path:
            raise ValueError("Error: File path is not specified.")
        if not os.path.exists(file_path):
            raise ValueError(f"Error: File '{file_path}' not found or does not exist.")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                if len(lines) < 2:
                    raise ValueError("Error: The file is too short.")
                if has_header:
                    header = lines[0].strip().split(",")
                    if len(header) != 2 or not all(part.isalpha() for part in header):
                        raise ValueError("Error: Invalid header format.")
                    data_lines = lines[1:]
                else:
                    data_lines = lines
                data = []
                for _, line in enumerate(data_lines, start=1):
                    values = line.strip().split(",")
                    if len(values) != 2:
                        raise ValueError("Error: Incorrect data format.")
                    if not all(v in {"0", "1"} for v in values):
                        raise ValueError("Error: Value in line is not correct.")
                    data.append([int(val) for val in values])
                return data
        except Exception as e:
            print(e)
            exit(1)

    class Calculations:
        @staticmethod
        def counts(data_list):
            heads, tails = 0, 0
            for row in data_list:
                if row[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            percent_heads = (heads / total) * 100 if total else 0
            percent_tails = (tails / total) * 100 if total else 0
            return percent_heads, percent_tails

        @staticmethod
        def predict_last(data_list):
            if not data_list:
                raise ValueError("Error: No data to predict.")
            return data_list[-1]


class Analytics(Research.Calculations):

    @staticmethod
    def predict_random(n):
        predictions = []
        for _ in range(n):
            if randint(0, 1) == 0:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        return predictions

    @staticmethod
    def save_file(data, file_name, extension):
        full_name = f"{file_name}.{extension}"
        with open(full_name, "w") as f:
            f.write(data)