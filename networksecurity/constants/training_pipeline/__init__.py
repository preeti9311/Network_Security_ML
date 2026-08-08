import os
import sys
import numpy as np
import pandas as pd

"""
defining some common constant variables for the training pipeline

"""
TARGET_COLUMN ="Result"
PIPELINE_NAME:str ="NetworkSecurity"
ARTIFACT_DIR:str="artifact"
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

"""
Constants for the training pipeline. data ingestion related constants start with data _ingestion var name
"""

DATA_INGESTION_COLLECTION_NAME : str="PhishingData"
DATA_INGESTION_DATABASE_NAME : str="NetworkSecurity"
DATA_INGESTION_DIR_NAME : str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str="feature_store"
DATA_INGESTION_INGESTED_DIR : str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float=0.2


DATA_VALIDATION_DIR_NAME : str="data_validation"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str="report.yaml"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str="drift_report"


## schema file path 
SCHEMA_FILE_PATH =os.path.join("data_schema","schema.yaml")

