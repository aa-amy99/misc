import mysql.connector

conn = mysql.connector.connect(option_files = './etc/my.cnf')
print('success')
cursor = conn.cursor()

query = "select year, title " \
        "from oscarval_sql_course.imdb_movies " \
        "limit 7;"
print(query)
cursor.execute(query)

for (year, title) in cursor:
    print(year, title)
conn.close()

