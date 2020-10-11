#! /usr/bin/env python3

import requests
import argparse
import pandas as pd
import json


def get_balance_sheet(stock_symbol):
    """ get the cash flow data
        
        args:
            ticker: US stock symbol
        
        returns:
            df_annual: annual income statement data, 
            df_quarterly: quaterly income statement data

            datafarme with columns:
            ['fiscalDateEnding', 'reportedCurrency', 'totalAssets',
            'intangibleAssets', 'earningAssets', 'otherCurrentAssets',
            'totalLiabilities', 'totalShareholderEquity',
            'deferredLongTermLiabilities', 'otherCurrentLiabilities', 'commonStock',
            'retainedEarnings', 'otherLiabilities', 'goodwill', 'otherAssets',
            'cash', 'totalCurrentLiabilities', 'shortTermDebt',
            'currentLongTermDebt', 'otherShareholderEquity',
            'propertyPlantEquipment', 'totalCurrentAssets', 'longTermInvestments',
            'netTangibleAssets', 'shortTermInvestments', 'netReceivables',
            'longTermDebt', 'inventory', 'accountsPayable', 'totalPermanentEquity',
            'additionalPaidInCapital', 'commonStockTotalEquity',
            'preferredStockTotalEquity', 'retainedEarningsTotalEquity',
            'treasuryStock', 'accumulatedAmortization', 'otherNonCurrrentAssets',
            'deferredLongTermAssetCharges', 'totalNonCurrentAssets',
            'capitalLeaseObligations', 'totalLongTermDebt',
            'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities',
            'negativeGoodwill', 'warrants', 'preferredStockRedeemable',
            'capitalSurplus', 'liabilitiesAndShareholderEquity',
            'cashAndShortTermInvestments', 'accumulatedDepreciation',
            'commonStockSharesOutstanding']

    """
    api_key = "Y4DEWAV3C4XYQ9YA"
    url = "https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={}&apikey={}".format(
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
    parser = argparse.ArgumentParser(description="crawl balance sheet from one stock symbol")
    parser.add_argument("stock_symbol", type=str, help="stock symbol")
    args = parser.parse_args()
    annualReports, quaterlyReports = get_balance_sheet(args.stock_symbol)
    print(annualReports)
    print(quaterlyReports)
    print(quaterlyReports.columns)


if __name__ == "__main__":
    main()
