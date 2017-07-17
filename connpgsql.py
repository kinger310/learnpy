# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:50:43 2017

@author: Wangdi
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.02)
plt.plot(x, x**2, 'r^', x, x**3, 'bo', x, x, 'y-')
plt.show()

# TODO test postpresql
import sqlalchemy


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    # postgresql+psycopg2
    # postgresql://postgres:root@localhost:5432/postgres/test
    # postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con)
    return con, meta

if __name__ == '__main__':
    con, meta = connect('postgres', 'root', 'postgres')

    import pandas as pd
    # pd.read_sql('SELECT datname FROM pg_database;', con)
    df = pd.read_sql('SELECT * FROM tips;', con)

