#! /usr/env/bin python3


import sqlite3
import argparse
import pandas as pd
import os
import datetime

import commons
import database
import us_symbol_crawler
import income_statement_crawler
import cash_flow_crawler
import balance_sheet_crawler


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
    if database.check_table_exist(conn, "symbol"):
        print("to be done")
    else:
        # assign UID to every symbol
        symbol_df["UID"] = pd.Series(range(0, symbol_df["symbol"].count()))
        symbol_df.to_sql("symbol", con=conn, if_exists="replace")

    c = conn.cursor()
    c.execute("SELECT symbol, UID FROM symbol")
    print(c.fetchmany(10))
    # print(c.fetchall())


def update_all(conn, stock_symbol):
    update_income_statement(conn, stock_symbol)


def main():
    parser = argparse.ArgumentParser(description="update data [one stock symbol]")
    parser.add_argument("--database", type=str, default=commons.DATABASE_FILE)
    parser.add_argument(
        "stock_symbol",
        type=str,
        default=[],
        nargs="?",
        help="stock symbols, or empty to update for all US symbol",
    )
    args = parser.parse_args()
    conn = sqlite3.connect(args.database)

    symbol_df = us_symbol_crawler.get_updated_symbols()
    update_symbol(conn, symbol_df)
    """
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
    """


if __name__ == "__main__":
    main()
