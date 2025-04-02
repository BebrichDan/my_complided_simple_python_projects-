import sys

def get_companies():
  companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
  }
  reverse_dict_companies = {v: k for k, v in companies.items()}  
  return companies, reverse_dict_companies

def get_stocks():
  return {
  'AAPL': 287.73,
  'MSFT': 173.79,
  'NFLX': 416.90,
  'TSLA': 724.88,
  'NOK': 3.37
  }

def get_stock_price(company_ticker):

  _, reverse_dict_company = get_companies()
  stocks = get_stocks()

  company_ticker_upp = company_ticker.upper()

  stock_symbol = stocks.get(company_ticker_upp)
  company_name = reverse_dict_company.get(company_ticker_upp)

  if company_name:
    print(company_name, stock_symbol)
  else:
    print("Unknown ticker")

if __name__ == '__main__':
    if len(sys.argv) == 2: 
        company_ticker = sys.argv[1]  
        get_stock_price(company_ticker)