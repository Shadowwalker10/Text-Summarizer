from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

## Creating the pipeline

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        dataset_ingestion = DataIngestion(data_ingestion_config)
        dataset = dataset_ingestion.get_data()
        return dataset
