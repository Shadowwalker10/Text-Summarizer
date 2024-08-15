from textSummarizer.logging import logger
import torch
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME} Started>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    dataset = data_ingestion.main()
    logger.info(f"<<<<<{STAGE_NAME} Completed>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME} Started>>>>>")
    data_transformation = DataTransformationTrainingPipeline()
    dataset_encoded = data_transformation.main()
    logger.info(f"<<<<<{STAGE_NAME} Completed>>>>>")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME} Started>>>>>")
    torch.cuda.empty_cache()
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"<<<<<{STAGE_NAME} Completed>>>>>")
    

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME} Started>>>>>")
    torch.cuda.empty_cache()
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"<<<<<{STAGE_NAME} Completed>>>>>")

except Exception as e:
    logger.exception(e)
    raise e

