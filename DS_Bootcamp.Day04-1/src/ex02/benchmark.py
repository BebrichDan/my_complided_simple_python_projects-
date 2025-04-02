import timeit 
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

def get_emails_cyclically(emails_list):
    result = []
    for email in emails_list:
        if "@gmail" in email:
            result.append(email)
    return result

def get_emails_list_comprehansion(emails_list):
    result = [email for email in emails_list if "@gmail" in email]
    return result

def get_emails_with_map(emails_list):
    result = map(lambda x: x if "@gmail" in x else None, emails_list)
    return [email for email in result if email is not None]

def get_emails_with_filter(emails_list):
    return list(filter(lambda x: "@gmail" in x, emails_list))


if __name__ == '__main__':

    if(len(sys.argv) != 3):
        raise ValueError("Incorrect quantity arguments. Correctly: benchmark.py <tested_function> <quantity_calls>")
    
    functions_nick = {
        "loop" : "get_emails_cyclically",
        "list_comprehension" : "get_emails_list_comprehansion",
        "map" : "get_emails_with_map",
        "filter" : "get_emails_with_filter",
    }

    tested_function = sys.argv[1]
    quantity_calls = int(sys.argv[2])

    str_stmt = f"{functions_nick[tested_function]}(emails)"
    print(timeit.timeit(stmt=str_stmt, globals=globals(), number=quantity_calls))