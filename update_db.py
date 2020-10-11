#! /usr/env/bin python3


import sqlite3
import argparse
import pandas as pd
import os


import us_symbol_crawler
import income_statement_crawler
import cash_flow_crawler
import balance_sheet_crawler


def check_table_exist(conn, table_name):
    c = conn.cursor()

    # get the count of tables with the name
    c.execute(
        """ SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' """.format(
            table_name
        )
    )

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print("{} table exists.".format(table_name))
        return True
    else:
        print("{} table not exists.".format(table_name))
        return False


def update_income_statement(conn, stock_symbol):
    """ update one stock's income statement
    """
    table_name_annaul = stock_symbol + "_annual_income_statement"
    table_name_quarterly = stock_symbol + "_income_statement"
    print("to do done")


def update_cash_flow(conn, stock_symbol):
    """ update one stock's cash flow
    """
    print("to do done")


def update_balance_sheet(conn, stock_symbol):
    """ update one stock's balance sheet
    """
    print("to do done")


def update_symbol(conn, symbol_df):
    """update symbols
    """
    print("to do done")


def update_all(conn, stock_symbol):
    update_income_statement(conn, stock_symbol)


def main():
    parser = argparse.ArgumentParser(description="update data [one stock symbol]")
    parser.add_argument("--database", type=str, default="us_stock_etf.db")
    parser.add_argument(
        "stock_symbol",
        type=str,
        default=[],
        nargs="+",
        help="stock symbols, or empty to update for all US symbol",
    )
    args = parser.parse_args()
    conn = sqlite3.connect(args.database)

    symbol_df = us_symbol_crawler.get_updated_symbols()
    update_symbol(conn, symbol_df)
    if not args.stock_symbol:
        # updata all
        print("to be done")
    else:
        for symbol in args.stock_symbol:
            try:
                symbol_df.loc[symbol]
                update_all(conn, symbol)
            except:
                print("{} is not a valid symbol".format(symbol))


if __name__ == "__main__":
    main()
