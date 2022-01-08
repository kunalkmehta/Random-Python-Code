import os
import pandas as pd
from google.cloud import bigquery


os.chdir(r'C:/RnD/BigQuery/Project')

client = bigquery.Client.from_service_account_json('connect_gcp.json')
table_id ="<your table id>"
job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)


with open('Loyalty Card.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)


