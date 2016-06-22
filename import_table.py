from database import get_tables
from database import execute
from xlsxhelper import write_document
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        table_name = sys.argv[1]
        try:
            query = "SELECT * FROM {0}".format(table_name)
            results = execute(query)
            write_document("data/{0}.xlsx".format(table_name), results)
            print("{0}.xlsx imported".format(table_name))
        except Exception as e:
            print(e)
            print("import failed.")
    else:
        print("Usage: python import_table.py [table_name]")
