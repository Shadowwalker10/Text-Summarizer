from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modeltrainer import ModelTrainer
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        data_transformation = DataTransformationTrainingPipeline()
        dataset = data_transformation.main()
        model_trainer_config = ModelTrainer(model_trainer_config, dataset = dataset)
        model_trainer_config.train()