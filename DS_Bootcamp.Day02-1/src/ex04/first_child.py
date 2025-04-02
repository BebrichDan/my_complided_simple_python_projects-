import sys
from random import randint
sys.path.append("../ex03")  

from first_nest import Research

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
    def predict_last(data):
        if not data:
            raise ValueError("Error: Data list is empty.")
        
        return data[-1]

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

    data_random = Analytics.predict_random(3)
    print(data_random) 
    last_element = Analytics.predict_last(return_list)
    print(last_element)
