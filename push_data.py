import os
import sys
import json

from dotenv import load_dotenv
# ye .env file ko load karta hai.
load_dotenv()

# Environment variable ki value nikalta hai.
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract:
    
    def __init__(self):
        try:
            pass
        except Exception as e:
            logger.logging.error("Failed to create MongoDB client.")
            raise NetworkSecurityException(e, sys)

    def cv_to_json(self, cv_file_path):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(cv_file_path)
            df.reset_index(drop=True,inplace=True)
            logger.logging.info(f"CSV file '{cv_file_path}' read successfully.")
            
            # Convert the DataFrame to JSON format
            json_data=list(json.loads(df.T.to_json()).values())
            logger.logging.info("DataFrame converted to JSON format successfully.")
            
            return json_data  # Return as a list of dictionaries
        except Exception as e:
            logger.logging.error(f"Failed to convert CSV to JSON: {e}")
            raise NetworkSecurityException(e, sys)

    def insert_data(self, json_data, database, collection):
        try:
            self.database = database
            self.collection=collection
            self.json_data=json_data

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.json_data)

            return (len(self.json_data))

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NetworkSecurity"
    Collection="PhishingData"
    network_data_extract=NetworkDataExtract()
    json_data=network_data_extract.cv_to_json(FILE_PATH)
    no_of_records=network_data_extract.insert_data(json_data,DATABASE,Collection)
    print(no_of_records)