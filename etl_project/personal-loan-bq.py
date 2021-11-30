from google.cloud import bigquery
import os

#Set up bq
client = bigquery.Client(project="personal-loan-bq")
target_table = "personal-loan-bq.bank_data.bank_table"

#Load csv data to BQ
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE' #overwrite it, write_append, write_empty fpr no duplicate
)

#file_path
file_path = os.path.join(os.getcwd(),"data", "bank_personal_loan.csv")
with open(file_path, 'rb') as srcfile:
    load_job = client.load_table_from_file(srcfile, target_table, job_config=job_config)

load_job.result()
des_table = client.get_table(target_table)
print(client.get_table(target_table).num_rows)

