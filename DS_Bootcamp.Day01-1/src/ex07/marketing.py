import sys

def get_clients():
    return ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

def get_participants():
    return ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

def get_recipients():
    return ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def processing(name_call):
    clients = set(get_clients())
    events = set(get_participants())
    viewed = set(get_recipients())
    if name_call == "call_center" :
        call_center = (clients|events) - viewed
        print(call_center)
    elif name_call == "potential_clients":
        potential_clients = (events - clients)
        print(potential_clients)
    elif name_call == "loyalty_program":
        loyalty_program = clients - events
        print(loyalty_program)
    else:
        raise ValueError("This call is not difined!")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        processing(sys.argv[1])