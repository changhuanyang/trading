#! /usr/bin/env python3

import urllib
import tempfile
import argparse
import pandas as pd
import os
from ftplib import FTP
import datetime

import commons


def get_us_symbols():
    """get us all equity and ETF symbols/companyName

    return:
        all_us_symbols: a dataframe with columns Symbol, Company, ETF

    """

    def get_nasdaq_symbols(data_buffer):
        ftp = FTP("ftp.nasdaqtrader.com")
        ftp.login()
        ftp.cwd("symboldirectory")
        ftp.retrbinary("RETR nasdaqlisted.txt", data_buffer.write)
        data_buffer.seek(0)
        df = pd.read_csv(data_buffer, delimiter="|", skipfooter=1)
        df = df.filter(items=["Symbol", "Security Name", "ETF"])
        df = df[df["ETF"].notnull()]
        df["ETF"] = df["ETF"].map({"Y": True, "N": False})
        df = df.rename(columns={"Security Name": "Company"})
        df = df.set_index("Symbol")
        return df

    def get_other_symbols(data_buffer):
        ftp = FTP("ftp.nasdaqtrader.com")
        ftp.login()
        ftp.cwd("symboldirectory")
        ftp.retrbinary("RETR otherlisted.txt", data_buffer.write)
        data_buffer.seek(0)
        df = pd.read_csv(data_buffer, delimiter="|", skipfooter=1)
        df = df.filter(items=["ACT Symbol", "Security Name", "ETF"])
        df = df[df["ETF"].notnull()]
        df["ETF"] = df["ETF"].map({"Y": True, "N": False})
        df = df.rename(columns={"Security Name": "Company", "ACT Symbol": "Symbol"})
        df = df.set_index("Symbol")
        return df

    with tempfile.TemporaryFile() as fp:
        nasdaq_df = get_nasdaq_symbols(fp)
    with tempfile.TemporaryFile() as fp:
        other_df = get_other_symbols(fp)
    all_symbol_df = pd.concat([nasdaq_df, other_df])
    return all_symbol_df


def symbol_need_update():
    if os.path.exists(commons.UPDATE_SYMBOL_FILE):
        last_update_date = datetime.date.fromtimestamp(os.path.getmtime(commons.UPDATE_SYMBOL_FILE))
        today = datetime.date.today()
        time_period = today - last_update_date
    return time_period > datetime.timedelta(days=1)


def get_updated_symbols():
    if symbol_need_update():
        all_symbol_df = get_us_symbols()
        all_symbol_df.to_csv(commons.UPDATE_SYMBOL_FILE)
    else:
        all_symbol_df = pd.read_csv(commons.UPDATE_SYMBOL_FILE)
        all_symbol_df = all_symbol_df.set_index("Symbol")
    return all_symbol_df


def main():
    parser = argparse.ArgumentParser(description="crawl all us trabale stock/etf symbols")
    args = parser.parse_args()
    if symbol_need_update():
        all_symbol_df = get_us_symbols()
        all_symbol_df.to_csv(commons.UPDATE_SYMBOL_FILE)
        print("write output to {}".format(commons.UPDATE_SYMBOL_FILE))
    else:
        print("Don't need to update symbols")


if __name__ == "__main__":
    main()

