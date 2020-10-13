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
        c = conn.cursor()
        for row in c.execute("SELECT MAX(stockUID) FROM symbol"):
            new_stockUID = row[0] + 1

        for index, symbol in symbol_df["symbol"].items():
            c.execute("SELECT COUNT(1) FROM symbol WHERE symbol='{}'".format(symbol))
            res = c.fetchone()
            if not res[0]:  # an unseen symbol
                # Insert a row of data
                values = [str(value) for value in symbol_df.iloc[index].to_list()]
                values.append(new_stockUID)
                is_ETF = 0 if values[2] is "False" else 1
                values = "'{}','{}',{},'{}',{}".format(
                    values[0], values[1], is_ETF, values[3], new_stockUID
                )
                sql = "INSERT INTO symbol (symbol, company, ETF, Exchange, stockUID) VALUES ({})".format(
                    values
                )
                print(sql)
                c.execute(sql)
                # Save (commit) the changes
                conn.commit()

                new_stockUID += 1
    else:
        symbol_df["stockUID"] = pd.Series(range(0, symbol_df["symbol"].count()))
        symbol_df.to_sql("symbol", con=conn, if_exists="replace")


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
    print(symbol_df.head())
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
