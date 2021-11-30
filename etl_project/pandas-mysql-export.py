import mysql.connector
import pandas as pd
import os


conn = mysql.connector.connect(option_files = './etc/my.cnf')

query1 = "select year, title,  avg_vote " \
        "from oscarval_sql_course.imdb_movies " \
        "where year between 2005 and 2006 " \
        "limit 10;"

# add new column (tranfrom ocuurred during extract step)
query2 = "select year, title,  avg_vote , case " \
         "      when avg_vote < 3 then 'bad' " \
         "      when avg_vote >=3 then 'good' " \
         "      end as movie_rating "\
         "from oscarval_sql_course.imdb_movies " \
         "where year between 2005 and 2006 " \
         "limit 1000;"

df = pd.read_sql(query2, conn)
yr_2005 = df['year'] == 2005

#speacify export path
cur_path = os.getcwd()
fname = 'movies_2005.csv'
f_path = os.path.join(cur_path, 'data', fname)
print(f_path)

df[df['year'] == 2005].to_csv(f_path , index = False)
conn.close()