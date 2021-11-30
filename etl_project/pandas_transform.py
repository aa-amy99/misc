import pandas as pd
import mysql.connector
import os

conn = mysql.connector.connect(option_files = './etc/my.cnf')

query = "select * " \
        "from oscarval_sql_course.city_house_prices " \

#data transformation
df = pd.read_sql(query, conn)
df.set_index('Date', inplace=True)
df = df.stack().reset_index()
df.columns = ['date', 'city', 'price']
print(df.head())

fpath = os.path.join(os.getcwd(), 'data', 'city_house.csv')
df.to_csv(fpath, index=False)

conn.close()
