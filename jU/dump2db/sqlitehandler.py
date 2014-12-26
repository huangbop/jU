"""
"""

import os
import sqlite3

from utils import dump2db_get_logger, generate_db_name

__all__ = [
    "Dump2dbSqliteHandler",
]



logger = dump2db_get_logger()

class Dump2dbSqliteHandler():
    """
    """

    def initiator(self, rows):
        conn = self.create_conn()
        
        self.dump_simple_registration(rows, conn)
        conn.close()

    def create_conn(self):
        name = generate_db_name()
        conn = sqlite3.connect(name)
        return conn

    def dump_simple_registration(self, rows, conn):
        
        
        logger.warning('Dump simple registration OK.')






