import timeit
import sys
from functools import reduce

def squaring_with_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def squaring_with_reduce(n):
    return reduce(lambda sum, number: sum + number ** 2, range(1, n+1), 0)
    

if __name__ == '__main__':

    if(len(sys.argv) != 4):
        raise ValueError("Incorrect quantity arguments. Correctly: benchmark.py <tested_function> <quantity_calls> <sum_squaries>")
    
    tested_function = sys.argv[1]
    quantity_calls = int(sys.argv[2])
    sum_squaries = int(sys.argv[3])

    if tested_function == "loop":
        print(timeit.timeit(stmt=f"squaring_with_loop({sum_squaries})", globals=globals(), number=quantity_calls))
    elif tested_function == "reduce":   
        print(timeit.timeit(stmt=f"squaring_with_reduce({sum_squaries})", globals=globals(), number=quantity_calls))
    else:
        raise ValueError(f"There is no function '{tested_function}' for testing")