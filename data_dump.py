# Why this file? In industry we are not upload the dataset in local.
# We will get this on cloud, so we pushing our data into mongodb

import pymongo
import pandas as pd
import json # Because data mongodb la json format la irukum

client = pymongo.MongoClient("mongodb+srv://santhosh:Nandhini@cluster0.z35j0ax.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\msant\Insurance-Premium-Prediction\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT" #table name

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}") #Checking database shapes

    df.reset_index(drop=True, inplace=True) #Dropping index column

    json_records = list(json.loads(df.T.to_json()).values()) # JSon data la key values pairs ah irukum nu sonnanga
    print(json_records[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records) # Inserting data into mongodb, Now go and check on mongodb too