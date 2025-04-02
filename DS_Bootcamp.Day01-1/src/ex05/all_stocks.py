import sys

def get_companies():
    return {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}

def get_stocks():
    return {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}

def defining_input_values(string):

    company = get_companies()
    stocks = get_stocks()

    if len(sys.argv) != 2 or ",," in string or ", ," in string:
        return
    
    res_string = [s.strip() for s in string.split(',')]

    for item in res_string:
        if item.lower() in [key.lower() for key in company.keys()]:
            for j in company.keys():
                if j.lower() == item.lower():
                    stock_symbol = company[j]
                    price = stocks.get(stock_symbol)
                    print(f"{j} stock price is {price}")
        elif item.lower() in [value.lower() for value in company.values()]:
            for j in company.values():
                if j.lower() == item.lower():
                    company_name = (next((key for key, value in company.items() if value.lower() == item.lower()), None))
                    print(f"{j} is a ticker symbol for {company_name}")
        else:
            print(f"{item} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        defining_input_values(sys.argv[1])