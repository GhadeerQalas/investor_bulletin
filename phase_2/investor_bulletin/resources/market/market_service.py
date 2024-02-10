""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import requests
from requests.exceptions import HTTPError
import time
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class MarketService:
    """
    Purpose: initializes the MarketService class with the list of symbols and the API URL
    """
    def __init__(self):
        self.api_url = "https://twelve-data1.p.rapidapi.com/price"
        self.headers = {
            'X-RapidAPI-Key': os.getenv('RapidAPI_Key'),
            'X-RapidAPI-Host': os.getenv('RapidAPI_Host')
        }

    """
    Purpose: fetches the market data for the list of symbols
    Returns: list of dictionaries containing the symbol and the price
    """
    def get_market_data(self, symbols):
        stock_prices = []
        for symbol in symbols:
            status_code, price = self.get_price_for_symbol(symbol)
            if price is not None and status_code == 200:
                stock_prices.append({'symbol': symbol, 'price': price})
            else:
                stock_prices.append({'symbol': symbol, 'price': price})
                print(f'Error occurred while fetching data for {symbol}')
        return stock_prices

    """
    Purpose: fetches the price for a given symbol
    Returns: the status code and the price
    """
    def get_price_for_symbol(self, symbol):
        querystring = {
            "symbol": symbol,
            "outputsize": "30",
            "format": "json"
        }
        try:
            print(f'Fetching data for {symbol}...', self.headers)
            response = requests.request("GET", self.api_url, headers=self.headers, params=querystring)
            response.raise_for_status()
            return response.status_code, response.json()['price']
        except HTTPError as http_err:
            status_code = http_err.response.status_code
            if status_code == 429:
                print('Rate limit exceeded. Waiting for 60 seconds before retrying...')
                time.sleep(60)  # wait for 60 seconds
                return self.get_price_for_symbol(symbol)  # retry the request
            else:
                print(f'HTTP error occurred: {http_err}')
                return status_code, 'HTTP error occurred: {http_err}'
        except Exception as err:
            print(f'An error occurred: {err}')
            return 400, 'HTTP error occurred: {err}'
