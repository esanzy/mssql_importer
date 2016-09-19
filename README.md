## installing odbc on mac

```
brew install /homebrew/versions/freetds091
```

```
brew install unixodbc
```

## freetds config

```
sudo vi /usr/local/Cellar/freetds/(version)/etc/freetds.conf
```

## unixodbc config

```
sudo vi /usr/local/Cellar/unixodbc/(version)/etc/odbc.ini
```

```
sudo vi /usr/local/Cellar/unixodbc/(version)/etc/odbcinst.ini
```

config file examples in source code


## virtual environment setting

```
virtualenv -p python3 myenv
```

(use python3, it is very important to process non-ascii characters from DB)

```
source myenv/bin/activate
```

```
pip install pymssql
```

```
pip install xlsxwriter
```

## how to run

1. import table list to excel file

```
python import_table_list.py
```

2. import specific table data

```
python import_table.py [table name]
```

3. import all tables

```
python import_all_tables.py
```

have fun!
