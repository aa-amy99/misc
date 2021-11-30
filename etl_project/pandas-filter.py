import mysql.connector
import pandas as pd

conn = mysql.connector.connect(option_files = './etc/my.cnf')

query = "select year, title,  avg_vote " \
        "from oscarval_sql_course.imdb_movies " \
        "where year between 2005 and 2006 " \
        "limit 10;"

df = pd.read_sql(query, conn)
yr_2005 = df['year'] == 2005
print(yr_2005.head())
print(df[~yr_2005].head())

conn.close()