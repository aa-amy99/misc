import os
import pandas
import mysql.connector
import pandas as pd
from google.cloud import bigquery

#1. set var
#SQL
curr_path = os.getcwd()
load_file = 'mysql_export.csv'
load_file = os.path.join(curr_path, 'data', load_file)

#BQ
proj = 'firstproject-330801'
dat = 'dat1'
target_table = 'annual_movie_summary'
table_id=f'{proj}.{dat}.{target_table}'

#2. Data connection

conn = mysql.connector.connect(option_files = './etc/my.cnf')
client = bigquery.Client(project=proj)


# EXTRACT #########
# create SQL extract query
sql = """select year, count(imdb_title_id) as movie_count 
        , avg(duration) as avg_movie_duration
        , avg(avg_vote) as avg_rating 
        from oscarval_sql_course.imdb_movies 
        group by 1"""

df = pd.read_sql(sql, conn)


# TRANSFORM #########
def year_rating(r):
    if r <= 5.65: return 'bad movie'
    elif r >5.65: return 'good movie'
    else: return 'not rated'

df['year_rating'] = df['avg_rating'].apply(year_rating)
df.to_csv(load_file, index=False) #mysql_export.csv

# LOAD #########
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

#Open file for leading to BQ
with open(load_file, 'rb') as file:
    load_job= client.load_table_from_file(file, table_id, job_config = job_config)

load_job.result()
destination_table = client.get_table(table_id)
print(f"Total row: {destination_table.num_rows}")

