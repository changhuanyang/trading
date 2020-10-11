#! /usr/bin/env python3

import requests
import argparse
import pandas as pd
import json


def get_income_statement(stock_symbol):
    """ get the income_statement data
        
        args:
            symbol: US stock symbol
        
        returns:
            df_annual: annual income statement data, 
            df_quarterly: quaterly income statement data

            datafarme with columns:
            ['fiscalDateEnding', 'reportedCurrency', 'totalRevenue',
                'totalOperatingExpense', 'costOfRevenue', 'grossProfit', 'ebit',
            'netIncome', 'researchAndDevelopment', 'effectOfAccountingCharges',
            'incomeBeforeTax', 'minorityInterest', 'sellingGeneralAdministrative',
            'otherNonOperatingIncome', 'operatingIncome', 'otherOperatingExpense',
            'interestExpense', 'taxProvision', 'interestIncome',
            'netInterestIncome', 'extraordinaryItems', 'nonRecurring', 'otherItems',
            'incomeTaxExpense', 'totalOtherIncomeExpense', 'discontinuedOperations',
            'netIncomeFromContinuingOperations',
            'netIncomeApplicableToCommonShares',
            'preferredStockAndOtherAdjustments']

    """
    api_key = "Y4DEWAV3C4XYQ9YA"
    url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={}&apikey={}".format(
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
    parser = argparse.ArgumentParser(description="crawl income statement from stock symbol")
    parser.add_argument("stock_symbol", type=str, help="stock symbol")
    args = parser.parse_args()
    annualReports, quaterlyReports = get_income_statement(args.stock_symbol)
    print(annualReports)
    print(quaterlyReports)


if __name__ == "__main__":
    main()

