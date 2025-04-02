def convert_to_dict():
    list_of_tuples = get_list_of_tuples()

    result_dict = {}

    for country, number in list_of_tuples:
        if number in result_dict:
            result_dict[number].append(country)
        else:
            result_dict[number] = [country]

    for key, values in result_dict.items():
        for value in values:
            print(f"'{key}' : '{value}'")

def get_list_of_tuples():
    return [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
]


if __name__ == '__main__':
    convert_to_dict()