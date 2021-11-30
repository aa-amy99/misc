"""
@author: amy_a
"""

import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(option_files = './etc/my.cnf')
    print('success')
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('check credential')
    else:
        print('err')
