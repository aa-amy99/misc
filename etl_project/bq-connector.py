from google.cloud import bigquery

client = bigquery.Client(project = 'firstproject-330801')

sql = 'select * from dat1.movies_2005'
query_job = client.query(sql)
results = query_job.result()

for r in results:
    print(r.year, r.title)#2005 Lethal
    print(type(r), r)#<class 'google.cloud.bigquery.table.Row'> Row((2005, 'Lethal', 2.5, 'bad'), {'year': 0, 'title': 1, 'avg_vote': 2, 'movie_rating': 3})