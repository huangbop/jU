"""
"""

from sqlitehandler import *
from mongodbhandler import *

all = []

class InitializeHandlerException(Exception):
    '''An exception occur when initialize handler. '''
    
def main():
    try:
        dump2db_sqlite_handler = Dump2dbSqliteHandler()
    except:
        raise InitializeHandlerException
        
    dump2db_sqlite_handler.initiator(50)
    
if __name__ == '__main__':
    main()
