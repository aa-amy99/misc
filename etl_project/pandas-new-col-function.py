import pandas as pd
import mysql.connector
import os

conn = mysql.connector.connect(option_files = './etc/my.cnf')

query = "select year, title, avg_vote, case " \
        "when avg_vote <3 then 'bad' " \
        "when avg_vote >= 3 then 'good' " \
        "end as movie_rating, " \
        "duration " \
        "from oscarval_sql_course.imdb_movies " \
        "where year between 2005 and 2010 " \
        "limit 10;"

def movie_duration (d):
    if d < 60:
        return 'short_movie'
    else:
        return 'long_movie'
df = pd.read_sql(query, conn)
df['period'] = df['duration'].apply(movie_duration)
print(df.head())

fpath = os.path.join(os.getcwd(), 'data', 'movies_period.csv')
df['period'].to_csv(fpath, index = False)


conn.close()