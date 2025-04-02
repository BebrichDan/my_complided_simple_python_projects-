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
    result = ["@gmail" in email for email in emails_list]
    return result

if __name__ == '__main__':
    result_cyclically = timeit.timeit(stmt='get_emails_cyclically(emails)', globals=globals(), number=90000000)
    result_list_comprehension = timeit.timeit(stmt='get_emails_list_comprehansion(emails)', globals=globals(), number=90000000)
    if result_cyclically > result_list_comprehension:
        print("it is better to use a list comprehension")
        print(f"{result_list_comprehension} vs {result_cyclically}")
    else:
        print("it is better to use a loop")
        print(f"{result_cyclically} vs {result_list_comprehension}")
