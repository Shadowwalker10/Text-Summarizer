import os
from datasets import load_dataset
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def get_data(self):
        logger.info("Loading the dataset")
        self.dataset = load_dataset(self.config.data_to_load, trust_remote_code = True)
        logger.info("Data Loaded Successfully")
        return self.dataset