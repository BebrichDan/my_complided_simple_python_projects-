import timeit
import random
from collections import Counter

def genarotor_random_numbers(quantity=10000000, start_number=0, finish_number=100):
    randomer_numbers = []
    for _ in range(quantity):
        randomer_numbers.append(random.randint(start_number, finish_number))
    return randomer_numbers

def list_to_dict_count_number(list_random):
    result = {i: 0 for i in range(101)}
    for number in list_random:
        result[number] += 1
    return result

def popularity_numbers(list_random):
    popular_dict = list_to_dict_count_number(list_random)
    sorted_popular_dict = sorted(popular_dict.items(), key=lambda x: x[1], reverse=True)
    result_dict = sorted_popular_dict[:10]
    return result_dict


rand = genarotor_random_numbers()

print(f"my function: {timeit.timeit(stmt=f"list_to_dict_count_number(rand)", globals=globals(), number=1)}")
print(f"Counter: {timeit.timeit(stmt=f"c = Counter(rand)", globals=globals(), number=1)}")

c =  Counter(rand) #redifined
print(f"my top: {timeit.timeit(stmt=f"popularity_numbers(rand)", globals=globals(), number=1)}")
print(f"Counter's top: {timeit.timeit(stmt=f"c.most_common(10)", globals=globals(), number=1)}")
