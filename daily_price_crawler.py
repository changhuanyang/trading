#! /usr/bin/env python3

import requests
import argparse
import pandas as pd
import json


def get_daily_data(stock_symbol):
    """ get the daily data
        
        args:
            ticker: US stock symbol
        
        returns:
            df_daily: daily stock price dat
         
            datafarme with columns:
            ['open', 'high', 'low', 'close', 'adjusted_close', 'volume',
             'dividend_amount', 'split_coefficient']

    """
    api_key = "Y4DEWAV3C4XYQ9YA"
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}".format(
        stock_symbol, api_key
    )
    response = requests.get(url)
    dic = json.loads(response.text)

    df = pd.DataFrame.from_dict(dic["Time Series (Daily)"], orient="index")

    df = df.rename(
        columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. adjusted close": "adjusted_close",
            "6. volume": "volume",
            "7. dividend amount": "dividend_amount",
            "8. split coefficient": "split_coefficient",
        }
    )

    return df


def main():
    parser = argparse.ArgumentParser(description="crawl daily data from one stock symbol")
    parser.add_argument("stock_symbol", type=str, help="stock symbol")
    args = parser.parse_args()
    daily_data = get_daily_data(args.stock_symbol)
    print(daily_data)
    print(daily_data.columns)


if __name__ == "__main__":
    main()
