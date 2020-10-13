# Algorithm trading 




## DataBase Create/Update
Create a `us_stock_etf.db` if not exist and update certain symbol

Update all symbols from 
```bash
    $python update_db.py
```
Only Update certain symbol
```bash
    $python update_db.py symbol_1 symbol_2
```





## database design

there are 5 tables in the database

1. `symbol` : a table with columns ['symbol', 'company', 'ETF', 'exchange','stockUID']
2. `dailiy`: a table with columns ['stockUID', 'date', 'open', 'close', 'high', 'low', 'adjustedClose', 'volume', 'dividendAmount', 'splitCoefficient']
3. `quarterly_income_statement`: a table with columns ['stockUID', 'fiscalDateEnding', 'reportedCurrency', 'totalRevenue', 'totalOperatingExpense', 'costOfRevenue', 'grossProfit', 'ebit',
            'netIncome', 'researchAndDevelopment', 'effectOfAccountingCharges',
            'incomeBeforeTax', 'minorityInterest', 'sellingGeneralAdministrative',
            'otherNonOperatingIncome', 'operatingIncome', 'otherOperatingExpense',
            'interestExpense', 'taxProvision', 'interestIncome',
            'netInterestIncome', 'extraordinaryItems', 'nonRecurring', 'otherItems',
            'incomeTaxExpense', 'totalOtherIncomeExpense', 'discontinuedOperations',
            'netIncomeFromContinuingOperations',
            'netIncomeApplicableToCommonShares',
            'preferredStockAndOtherAdjustments']
4. `quarterly_cash_flow`: a table with columns ['stockUID', 'fiscalDateEnding', 'reportedCurrency', 'investments',
            'changeInLiabilities', 'cashflowFromInvestment',
            'otherCashflowFromInvestment', 'netBorrowings', 'cashflowFromFinancing',
            'otherCashflowFromFinancing', 'changeInOperatingActivities',
            'netIncome', 'changeInCash', 'operatingCashflow',
            'otherOperatingCashflow', 'depreciation', 'dividendPayout',
            'stockSaleAndPurchase', 'changeInInventory',
            'changeInAccountReceivables', 'changeInNetIncome',
            'capitalExpenditures', 'changeInReceivables', 'changeInExchangeRate',
            'changeInCashAndCashEquivalents']
5. `quarterly_balance_sheet`: a table with columns ['stockUID','fiscalDateEnding', 'reportedCurrency', 'totalAssets',
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


## Create virtual envrionment and install the required packages(If needed)

```bash 
    $./setup_venv.sh
```
If you already have all necessary packages listed in requriements.txt, you can pass this.


### miscellaneous

All US tradable symbols:

ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt
ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt

DatabaseDesign:
https://en.wikipedia.org/wiki/Database_normalization