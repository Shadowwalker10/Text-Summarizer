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
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories_and_files([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            tokenizer_name=config.tokenizer_name,
            train_size = config.train_size,
            test_size = config.test_size,
            validation_size=config.validation_size,
            input_encoding_length = config.input_encoding_length,
            target_encoding_length = config.target_encoding_length
        )
        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories_and_files([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            config.root_dir,
            config.model_ckpt,
            params.num_train_epochs,
            params.warmup_steps,
            params.per_device_train_batch_size,
            params.per_device_eval_batch_size,
            params.weight_decay,
            params.logging_steps,
            params.evaluation_strategy,
            params.eval_steps,
            params.save_steps,
            params.gradient_accumulation_steps,
            params.gradient_checkpointing,
            params.fp16
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories_and_files([config.root_dir])
        

        model_evaluation_config = ModelEvaluationConfig(config.root_dir, 
                                                        config.model_path, 
                                                        config.tokenizer_path, 
                                                        config.metrics_file_name)
        
        return model_evaluation_config