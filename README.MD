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



## Create virtual envrionment and install the required packages(If needed)

```bash 
    $./setup_venv.sh
```
If you already have all necessary packages listed in requriements.txt, you can pass this.


### miscellaneous

All US tradable symbols:

ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt
ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt