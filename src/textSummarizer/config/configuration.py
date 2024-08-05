from textSummarizer.constants import *
from textSummarizer.utils.common import create_directories_and_files, read_yaml
from textSummarizer.entity import *

class ConfigurationManager:
    def __init__(self, 
                 config_filepath = CONFIG_FILE_PATH, 
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        


        create_directories_and_files([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories_and_files([config.root_dir])
        

        data_ingestion_config = DataIngestionConfig(config.root_dir, 
                                                    config.data_to_load)
        
        return data_ingestion_config