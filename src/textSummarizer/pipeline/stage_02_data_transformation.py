from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config
                                                 #train_size=0.01, 
                                                 #test_size=0.03,
                                                 #validation_size=0.006
        )
        dataset_encoded = data_transformation.convert()
        return dataset_encoded
