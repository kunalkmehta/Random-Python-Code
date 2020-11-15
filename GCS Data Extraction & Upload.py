##### Extracting data from Google Cloud Storage Code Begins #####

##### Import libraries - Do install them if in case you don't have these libraries #####

from google.cloud import storage
import os
import pandas as pd
from io import StringIO

##### Change path #####

os.chdir(r'<Whatever path that you might want to put>')

pwd()

##### Connecting to your GCS account #####

storage_client= storage.Client.from_service_account_json('<Your JSON Service Account Key>')
bucket_name = '<Your Bucket Name>'
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.get_blob('customerdata.csv')

##### Check for data #####

if blob is None:
    print("No file found!")
else:
    print("Customer Data found!")

##### Extract CSV as DataFrame #####

downloaded_blob = blob.download_as_string()
s = str(downloaded_blob, 'utf-8')
data = StringIO(s)
df = pd.read_csv(data)

df.head()

##### Add data within DataFrame #####

df['test'] = 'Data Inserted'

df.head()

##### Connecting to your GCS account #####

bucket_name = '<Your Bucket Name>'
bucket = storage_client.get_bucket(bucket_name)
df.to_csv('updatedcustomerdata.csv', index = False)

##### Uplaoding data within GCS #####

filename = 'updatedcustomerdata.csv'
blob = bucket.blob(filename)
blob.upload_from_filename(filename)

##### Extracting data from Google Cloud Storage Code Ends #####