import timeit

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

if __name__ == '__main__':

    results = {
    "it is better to use a loop" : timeit.timeit(stmt='get_emails_cyclically(emails)', globals=globals(), number=90000000),
    "it is better to use a list comprehension" : timeit.timeit(stmt='get_emails_list_comprehansion(emails)', globals=globals(), number=90000000),
    "it is better to use a map" : timeit.timeit(stmt='get_emails_with_map(emails)', globals=globals(), number=90000000),
    }

    sorted_results = sorted(results.items(), key=lambda x: x[1])

    print(sorted_results[0][0])
    print(f"{sorted_results[0][1]} vs {sorted_results[1][1]} vs {sorted_results[2][1]}")

    


