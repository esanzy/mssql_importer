'''
Created on 2016. 8. 27.

@author: junwon
'''
from pymongo import MongoClient
from database import SQLDriver
import bson
from decimal import Decimal

client = MongoClient()
db = client['intercp']

if __name__ == "__main__":
    sqlserver = SQLDriver()

    for table in sqlserver.get_tables():
        table_name = table[2]
        if table_name not in ['WM_LOG', 'Sheet1$', 'LOGIN_LOG', 'bbsaa$', 'CMC_2011_ROOM$']:
            collection = db[table_name]
            collection.remove({})
            query = "SELECT * FROM {0}".format(table_name)

            try:
                rows = sqlserver.query_to_dict(query)
            except:
                print("Query: {0} fails".format(query))

            if rows is not None:
                count = 0
                for row in rows:
                    try:
                        collection.insert_one(row)
                        count += 1

                    except bson.errors.InvalidDocument as err:
                        for column, value in row.items():
                            if type(value) is Decimal:
                                row[column] = int(str(value))
                        try:
                            collection.insert_one(row)
                            count += 1
                        except Exception as err:
                            print(row)
                            print("row insertion failed.")
                            print(err)

                    except Exception as err:
                        print(row)
                        print("row insertion failed.")
                        print(err)

            print("Table {0}: {1} rows imported.".format(table_name, count))

    print("Complete")
    sqlserver.close()
    client.close()
