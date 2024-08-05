from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"<<<<<{STAGE_NAME} Started>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    dataset = data_ingestion.main()
except Exception as e:
    logger.exception(e)
    raise e
