import os.path
from google.cloud import bigquery

#Load data to table in BiqQuery

client = bigquery.Client(project = 'firstproject-330801')

target_table  = 'firstproject-330801.dat1.city_housing2'

job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    #detect type
    autodetect=True,
    write_disposition='WRITE_TRUNCATE' #overwrite it, write_append, write_empty fpr no duplicate
)

#file_path
file_path = os.path.join(os.getcwd(),"data", "city_house.csv")

with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(source_file,
                                           target_table,
                                           job_config=job_config)
#check if we load the job successfully
load_job.result()
destination_table = client.get_table(target_table)
print(f"Total row: {destination_table.num_rows}")