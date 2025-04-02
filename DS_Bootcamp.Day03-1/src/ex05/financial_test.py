#!/usr/bin/env python3
import time

import pytest
import requests
from bs4 import BeautifulSoup


def test_get_total_revenue():
    ticker = "MSFT"
    field = "Total Revenue"
    result = get_operating_income_data(ticker, field)

    assert result[0] == field, f"Expected '{field}', but got '{result[0]}'"

    assert len(result) > 1, "Expected multiple financial values in the tuple"

    for value in result[1:]:
        assert value.replace(",", "").isdigit(), f"Value {value} should be numeric"

def test_return_type():
    ticker = "AAPL"
    field = "Total Revenue"

    result = get_operating_income_data(ticker, field)

    assert isinstance(result, tuple), "Returned value should be a tuple"

def test_invalid_ticker():
    with pytest.raises(Exception) as exc_info:
        get_operating_income_data("INVALID", "Total Revenue")

    error_message = str(exc_info.value)
    assert "Error loading the page" in error_message or "Field 'Total Revenue' not found" in error_message, \
        f"Unexpected error message: {error_message}"


def get_operating_income_data(ticker: str, field: str) -> tuple:

    time.sleep(5)

    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
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

    
    # Запуск тестов: pytest -v