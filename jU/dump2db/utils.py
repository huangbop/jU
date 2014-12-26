
import os
import logging
import random
import string

__all__ = [
    "dump2db_get_logger"
]

def dump2db_get_logger():
    logger = logging.getLogger('jU.dump2db')
    return logger

def generate_db_name():
    name = ''.join(random.choice(string.ascii_uppercase) for i in range(16))
    return name + '.db'
    
    

    

