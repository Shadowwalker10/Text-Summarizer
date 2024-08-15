## Define pipeline
from textSummarizer.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modelevaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init(self):
        pass

    def main(self):
        
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        data_transformation = DataTransformationTrainingPipeline()
        dataset = data_transformation.main()
        
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config, dataset=dataset)
        model_evaluation_config.evaluate()
            