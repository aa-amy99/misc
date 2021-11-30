import mysql.connector
import pandas as pd

conn = mysql.connector.connect(option_files = './etc/my.cnf')
print('success')

query = "select year, title,  avg_vote " \
        "from oscarval_sql_course.imdb_movies " \
        "limit 1;"
print(query)

df = pd.read_sql(query, conn)
print (df.head())
print(df.dtypes)
print(df.columns)

for row in df.itertuples():
        print(row) #Pandas(Index=0, year=1906, title='The Story of the Kelly Gang', avg_vote=6.1)
        #print(row.year, type(row.year))
conn.close()