from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_ingestion import DataIngestion
import sys
from networksecurity.components.data_validation import DataValidation,DataValidationConfig



if __name__ == "__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)

        logging.info("Initiating data ingestion process...")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(f"Data ingestion artifact: {data_ingestion_artifact}")


        data_validation_config=DataValidationConfig(training_pipeline_config)
        Data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Initiating data validation process...")
        data_validation_artifact=Data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(f"Data validation artifact: {data_validation_artifact}")

    except Exception as e:
        raise NetworkSecurityException(e,sys)