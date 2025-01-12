import os
import sys
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import TrainingPipelineConfig , DataIngestionConfig , DataTransformationConfig , DataValidationConfig , ModelTrainerConfig
from networksecurity.entity.artifact_entity import *

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            logging.info("Start Data Ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.inititiate_data_ingestion()
            logging.info("Data ingestion completed !!!")
            
            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def start_data_validation(self) -> DataValidationArtifact:
        try:
            
            data_ingestion_artifact = self.start_data_ingestion()
            
            self.data_validation_config = DataValidationConfig(self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact , self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact
            
            

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def start_data_transformation(self) -> DataTransformationArtifact:
        try:
            data_validation_artifact = self.start_data_validation()

            self.data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact , self.data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()

            return data_transformation_artifact

            

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def start_model_training(self) -> ModelTrainerArtifact:
        try:
            data_transformation_artifact = self.start_data_transformation()

            self.model_training_config = ModelTrainerConfig(self.training_pipeline_config)
            model_trainer = ModelTrainer(self.model_training_config ,data_transformation_artifact )
            model_trainer_artifact = model_trainer.initiate_model_trainer()

            return model_trainer_artifact

            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact =self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_training(data_transformation_artifact=data_transformation_artifact)
            
    
            return model_trainer_artifact
    
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == "__main__":
    obj = TrainingPipeline()
    model_trainer_artifact = obj.run_pipeline()
        

