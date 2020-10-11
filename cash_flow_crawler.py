#! /usr/bin/env python3

import requests
import argparse
import pandas as pd
import json


def get_cash_flow(stock_symbol):
    """ get the cash flow data
        
        args:
            ticker: US stock symbol
        
        returns:
            df_annual: annual income statement data, 
            df_quarterly: quaterly income statement data

            datafarme with columns:
            ['fiscalDateEnding', 'reportedCurrency', 'investments',
            'changeInLiabilities', 'cashflowFromInvestment',
            'otherCashflowFromInvestment', 'netBorrowings', 'cashflowFromFinancing',
            'otherCashflowFromFinancing', 'changeInOperatingActivities',
            'netIncome', 'changeInCash', 'operatingCashflow',
            'otherOperatingCashflow', 'depreciation', 'dividendPayout',
            'stockSaleAndPurchase', 'changeInInventory',
            'changeInAccountReceivables', 'changeInNetIncome',
            'capitalExpenditures', 'changeInReceivables', 'changeInExchangeRate',
            'changeInCashAndCashEquivalents']

    """
    api_key = "Y4DEWAV3C4XYQ9YA"
    url = "https://www.alphavantage.co/query?function=CASH_FLOW&symbol={}&apikey={}".format(
        stock_symbol, api_key
    )
    response = requests.get(url)
    dic = json.loads(response.text)
    df_annual, df_quarterly = None, None
    if "annualReports" in dic:
        df_annual = pd.DataFrame(dic["annualReports"])
    if "quarterlyReports" in dic:
        df_quarterly = pd.DataFrame(dic["quarterlyReports"])

    return df_annual, df_quarterly


def main():
    parser = argparse.ArgumentParser(description="crawl cash flow from one stock symbol")
    parser.add_argument("stock_symbol", type=str, help="stock symbol")
    args = parser.parse_args()
    annualReports, quaterlyReports = get_cash_flow(args.stock_symbol)
    print(annualReports)
    print(quaterlyReports)
    print(quaterlyReports.columns)


if __name__ == "__main__":
    main()
