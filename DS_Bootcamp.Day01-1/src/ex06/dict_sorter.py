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

def sorted_and_print_list():
  country_codes = get_list_of_tuples()
  dict_country_codes = {country: int(number) for country, number in country_codes}
  sorted_countries = sorted(dict_country_codes.keys(), key=lambda country: (-dict_country_codes[country], country))
  for country in sorted_countries:
    print(country)


if __name__ == "__main__":
  sorted_and_print_list()
