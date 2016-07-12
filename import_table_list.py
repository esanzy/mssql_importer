from __future__ import unicode_literal
from database import get_tables
from xlsxhelper import write_document


if __name__ == "__main__":
    write_document("data/tables.xlsx", get_tables())
