import sys
import traceback
import pymssql  # @UnresolvedImport
import config


def exec_query(func):
    def wrapped(*args):
        try:
            return func(*args)
        except Exception as err:
            print("Exception: ", err)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print(''.join('!! ' + line for line in lines))
            raise err
    return wrapped


class SQLDriver:
    class __SQLDriver:
        def __init__(self):
            self.cnxn = pymssql.connect(config.host, config.userid, config.password, config.dbname)
            self.cursor = self.cnxn.cursor()

    instance = None

    def __init__(self):
        if not SQLDriver.instance:
            SQLDriver.instance = SQLDriver.__SQLDriver()

    def close(self):
        self.instance.cursor.close()
        self.instance.cnxn.close()

    @exec_query
    def execute(self, query):
        self.instance.cursor.execute(query)
        results = self.instance.cursor.fetchall()
        return results

    @exec_query
    def query_to_dict(self, query):
        self.instance.cursor.execute(query)
        columns = [column[0] for column in self.instance.cursor.description]
        results = []
        rows = self.instance.cursor.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results

    @exec_query
    def raw_query(self, query):
        self.instance.cursor.execute(query)
        if config.commit:
            self.instance.cnxn.commit()

    def get_tables(self):
        return self.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
