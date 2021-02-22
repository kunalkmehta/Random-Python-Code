######## Program Begins Here ########

#### Import Python libraries ####

import sqlite3
from google.cloud import storage 
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys

#### Establish Connetion ####

cnx = mysql.connector.connect(user='<Your User Name>', password='<Your Password>', host='<Your Public IP Adress of Cloud SQL>', 
                              database='<Your Database Name>')

cursor = cnx.cursor()

#### Connetion Established ####

#### Execute query ####

query1 = ("select * from customer")
cursor.execute(query1)


#### Create dataframe from resultant table ####
frame = pd.DataFrame(cursor.fetchall())

frame.head()

#### Put columns names for the dataframe ####

frame.columns = [['customer_id', 'age', 'gender', 'home_airport', 'ticket_num', 'passport_num', 'first_name', 'last_name', 
                 'email', 'cust_profile', 'tel']]

frame.head()

#### Inserting new records into the SQL table ####

new_cust = pd.read_csv("customers2.csv")

#### Inserting new records into the SQL table through For Loop ####

temp = 0
for i in range(len(new_cust)):
    customer_id = str(new_cust['customer_id'].iloc[i])
    age = int(new_cust['age'].iloc[i])
    gender = str(new_cust['gender'].iloc[i])
    home_airport = int(new_cust['home_airport'].iloc[i])
    ticket_num = str(new_cust['ticket_num'].iloc[i])
    passport_num = str(new_cust['passport_num'].iloc[i])
    first_name = str(new_cust['first_name'].iloc[i])
    last_name = str(new_cust['last_name'].iloc[i])
    email_addr = str(new_cust['email'].iloc[i])
    cust_profile = str(new_cust['cust_profile'].iloc[i])
    tel = str(new_cust['tel'].iloc[i])
    
    query2 = ("INSERT INTO customer (customer_id, age, gender, home_airport, ticket_num, passport_num, first_name,"
              " last_name, email_addr, tel, cust_profile)"
              "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    val = (customer_id, age, gender, home_airport, ticket_num, passport_num, first_name, last_name, email_addr, tel, 
           cust_profile)
    cursor.execute(query2, val)
    cnx.commit()
    temp = temp + 1
    print(temp, "Record Inserted for ",first_name )

#### Extremely Important: Close your SQL connection ####

cursor.close()
cnx.close()

######## Program Ends Here ########
