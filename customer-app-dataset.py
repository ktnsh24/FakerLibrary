#!/usr/bin/env python
# coding: utf-8

# # Install Faker Library
pip install Faker

#Python Libraries
import pandas as pd
import numpy as np
from faker import Faker

#Create Fake Customers Dataset
fake = Faker()
n = 1000
faker_data = pd.DataFrame([[fake.name(), 
                            fake.state(),
                           fake.date_of_birth(minimum_age =18, maximum_age = 65)] 
            for _ in range(n)],
            columns=['customer_name', 'customer_location', 'customer_birth_date' ])
faker_data['customer_id'] = range(1, 1+len(faker_data))
faker_data.head(30)


#Import App Dataset
filepath = "googleplaystore.csv" #Use your localpath
df = pd.read_csv(filepath ,encoding='utf-8')
col_name = ['app',  'category', 'rating', 'reviews', 'app_size', 'installs', 'app_type', 'price', 'content_rating', 'genres', 'last_updated', 'current_version', 'android_version']
df.columns = col_name
df.head(5)


# # Assign and Randomly Distribute customer_id to App Dataset
df["customer_id"] = np.random.randint(1, 1000, len(df))
df


#Merge Customer Data and App Data
customer_app_data = df.merge(faker_data, on='customer_id', how='left')
customer_app_data
