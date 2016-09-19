# from __future__ import unicode_literal
from database import get_tables
from database import execute
from xlsxhelper import write_document


if __name__ == "__main__":
    table_list = get_tables()

    for table in table_list:
        try:
            table_name = table[2]
            query = "SELECT * FROM {0}".format(table_name)
            results = execute(query)
            write_document("data/{0}.xlsx".format(table_name), results)
            print("{0}.xlsx imported".format(table_name))
        except:
            pass
