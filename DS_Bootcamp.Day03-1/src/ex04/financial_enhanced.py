#!/usr/bin/env python3
import sys
import time
import httpx  
from bs4 import BeautifulSoup

def get_operating_income_data(ticker: str, field: str) -> tuple:
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36"
    }

    response = httpx.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error loading the page: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    
    header_elem = soup.find(lambda tag: tag.name in ["div", "span"] and field == tag.get("title"))
    if not header_elem:
        raise Exception(f"Field '{field}' not found in the page.")
    
    row_container = header_elem.find_parent("div", class_=lambda x: x and "D(tbr)" in x)
    
    if not row_container:
        row_container = header_elem.parent.parent
  
    columns = row_container.find_all("div", class_=lambda x: x and "column" in x)
    if not columns or len(columns) < 2:
        raise Exception("Not enough columns found for the field data.")
    
    values = [col.get_text(strip=True) for col in columns]
    return tuple(values)


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise Exception("Arguments format: <program> <ticker> <field>")
    else:
        ticker = sys.argv[1]
        field = sys.argv[2]
    
    data = get_operating_income_data(ticker, field)
    print(data)