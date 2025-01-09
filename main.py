from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import sys
from networksecurity.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                  TrainingPipelineConfig,DataTransformationConfig)
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation


if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.inititiate_data_ingestion()
        logging.info("Data ingestion completed!!!")
        
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact , data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed!!!")
        
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact , data_transformation_config)
        logging.info("Initiate the data transformation...")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data transformation completed!!!")
        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
