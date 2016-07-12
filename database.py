import sys
import traceback
import pyodbc
import config


cnxn = pyodbc.connect("DSN={0};UID={1};PWD={2}".format(config.dsn, config.userid, config.password))
cursor = cnxn.cursor()


def exec_query(func):
    def wrapped(*args):
        global cnxn
        global cursor
        try:
            if not cnxn:
                cnxn = pyodbc.connect("DSN={0};UID={1};PWD={2}".format(config.dsn, config.userid, config.password))
                cursor = cnxn.cursor()
            return func(*args)
        except pyodbc.OperationalError as oerr:
            print("Operational Error: ", oerr)
            if cnxn:
                cnxn.close()
            raise oerr
        except pyodbc.ProgrammingError as perr:
            print("Programming Error: ", perr)
            if cnxn:
                cnxn.close()
            raise perr
        except Exception as err:
            print("Exception: ", err)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print(''.join('!! ' + line for line in lines))
            if cnxn:
                cnxn.close()
            raise err
    return wrapped


@exec_query
def execute(query):
    global cursor
    cursor.execute(query)
    results = cursor.fetchall()
    return results


@exec_query
def raw_query(query):
    global cursor
    cursor.execute(query)
    if config.commit:
        cnxn.commit()


def get_tables():
    return execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
