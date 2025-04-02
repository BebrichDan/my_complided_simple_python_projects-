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

def get_stock_price(company_name):

    if len(sys.argv) != 2:
        return

    companies = get_companies()
    stocks = get_stocks()

    stock_symbol = companies.get(company_name.title())
    price_stock = stocks.get(stock_symbol)

    if price_stock:
        print(price_stock)
    else:
        print("Unknown company")


if __name__ == '__main__': 
    stock_price = get_stock_price(sys.argv[1])



