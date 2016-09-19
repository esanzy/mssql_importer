# from __future__ import unicode_literal
from database import SQLDriver
from xlsxhelper import write_document


if __name__ == "__main__":
    db = SQLDriver()
    write_document("data/tables.xlsx", db.get_tables())

    for table in db.get_tables():
        print(table)
