#! /usr/bin/env python3

import tempfile
import pandas as pd
import os
from ftplib import FTP
import datetime

import commons


def get_us_symbols():
    """get us all equity and ETF symbols/companyName

    return:
        all_us_symbols: a dataframe with columns Symbol, Company, ETF, Exchange

    """

    def get_nasdaq_symbols(data_buffer):
        ftp = FTP("ftp.nasdaqtrader.com")
        ftp.login()
        ftp.cwd("symboldirectory")
        ftp.retrbinary("RETR nasdaqlisted.txt", data_buffer.write)
        data_buffer.seek(0)
        df = pd.read_csv(data_buffer, delimiter="|")
        df = df.filter(items=["Symbol", "Security Name", "ETF"])
        # last row is file_creation_time
        df_datetime = df.iloc[-1]
        datetime_row_num = df_datetime.name
        file_creation_time_str = df_datetime["Symbol"]
        # format: MMDDYYYYHH:mm
        file_creation_time_str = file_creation_time_str[(file_creation_time_str.find(":") + 1) :]
        file_creation_time_str = file_creation_time_str.strip()
        file_creation_time = datetime.date(
            int(file_creation_time_str[4:8]),
            int(file_creation_time_str[0:2]),
            int(file_creation_time_str[2:4]),
        )
        # drop file_creation_time row
        df = df.drop([datetime_row_num])
        df = df[df["ETF"].notnull()]
        df["ETF"] = df["ETF"].map({"Y": True, "N": False})
        df = df.rename(columns={"Security Name": "company", "Symbol": "symbol"})
        df["exchange"] = "Nasdaq"

        def remove_double_quotation(str):
            return str.strip('"')

        df["company"] = df["company"].apply(remove_double_quotation)

        return df, file_creation_time

    def get_other_symbols(data_buffer):
        ftp = FTP("ftp.nasdaqtrader.com")
        ftp.login()
        ftp.cwd("symboldirectory")
        ftp.retrbinary("RETR otherlisted.txt", data_buffer.write)
        data_buffer.seek(0)
        df = pd.read_csv(data_buffer, delimiter="|")
        df = df.filter(items=["ACT Symbol", "Security Name", "ETF", "Exchange"])
        # last row is file_creation_time
        df_datetime = df.iloc[-1]
        datetime_row_num = df_datetime.name
        file_creation_time_str = df_datetime["ACT Symbol"]
        # format: MMDDYYYYHH:mm
        file_creation_time_str = file_creation_time_str[(file_creation_time_str.find(":") + 1) :]
        file_creation_time_str = file_creation_time_str.strip()
        file_creation_time = datetime.date(
            int(file_creation_time_str[4:8]),
            int(file_creation_time_str[0:2]),
            int(file_creation_time_str[2:4]),
        )
        # drop file_creation_time row
        df = df.drop([datetime_row_num])

        df = df[df["ETF"].notnull()]
        df["ETF"] = df["ETF"].map({"Y": True, "N": False})
        df = df.rename(
            columns={"Security Name": "company", "ACT Symbol": "symbol", "Exchange": "exchange"}
        )
        df["exchange"] = df["exchange"].map(
            {"A": "NYSE MKT", "N": "NYSE", "P": "NYSE ARCA", "Z": "BATS", "Z": "IEXG"}
        )
        df = df[df["exchange"].notnull()]

        def remove_double_quotation(str):
            return str.strip('"')

        df["company"] = df["company"].apply(remove_double_quotation)
        return df, file_creation_time

    with tempfile.TemporaryFile() as fp:
        nasdaq_df, _ = get_nasdaq_symbols(fp)
    with tempfile.TemporaryFile() as fp:
        other_df, _ = get_other_symbols(fp)
    all_symbol_df = pd.concat([nasdaq_df, other_df])
    print(all_symbol_df.head())
    return all_symbol_df


def symbol_need_update():
    if os.path.exists(commons.UPDATE_SYMBOL_FILE):
        last_update_date = datetime.date.fromtimestamp(os.path.getmtime(commons.UPDATE_SYMBOL_FILE))
        today = datetime.date.today()
        time_period = today - last_update_date
        return time_period > datetime.timedelta(days=1)
    return True


def get_updated_symbols():
    if symbol_need_update():
        all_symbol_df = get_us_symbols()
        all_symbol_df.to_csv(commons.UPDATE_SYMBOL_FILE, index=False)
    else:
        all_symbol_df = pd.read_csv(commons.UPDATE_SYMBOL_FILE)
    return all_symbol_df


def main():
    all_symbol_df = get_us_symbols()
    all_symbol_df.to_csv(commons.UPDATE_SYMBOL_FILE)
    print("write output to {}".format(commons.UPDATE_SYMBOL_FILE))


if __name__ == "__main__":
    main()

