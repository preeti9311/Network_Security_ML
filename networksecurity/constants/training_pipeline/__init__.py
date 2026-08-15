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

SAVED_MODEL_DIR=os.path.join("saved_models")
MODEL_FILE_NAME="model.pkl"

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
PREPROCESSING_OBJECT_FILE_NAME :str= "preprocessor.pkl"

## schema file path 
SCHEMA_FILE_PATH =os.path.join("data_schema","schema.yaml")


"""
Constants for the data transformation pipeline
"""
DATA_TRANSFORMATION_DIR_NAME : str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str="preprocessed"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}


"""model trainer related constant start with mode trainer var name"""

MODEL_TRAINER_DIR_NAME: str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float=0.05



