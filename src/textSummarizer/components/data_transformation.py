import os
from textSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from ensure import ensure_annotations
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.config.configuration import ConfigurationManager as DataIngestionConfigManager



class DataTransformation:
    def __init__(self, 
                 config:DataTransformationConfig
                 #train_size:floatExpecting a percentage in decimal form
                 #test_size:float,# Expecting a percentage in decimal form
                 #validation_size:float,# Expecting a percentage in decimal form
                 #input_encoding_length:int = 32,
                 #target_encoding_length:int = 8
    ):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        self.input_encoding_length = config.input_encoding_length
        self.target_encoding_length = config.target_encoding_length
        self.train_size, self.test_size, self.validation_size = config.train_size, config.test_size, config.validation_size
        
    @ensure_annotations
    def convert_examples_features(self, 
                               example_batch,
                               ):
        input_encodings = self.tokenizer(text = example_batch["dialogue"],
                                         max_length = self.input_encoding_length,
                                         truncation = True, padding = "max_length"
                                         )
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(text = example_batch["summary"],
                                          max_length = self.target_encoding_length,
                                          truncation = True, padding = "max_length")
            
        return {
            "input_ids":input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"]
        }
    def convert(self):
        ingestion_config = DataIngestionConfigManager()
        data_ingestion_config = ingestion_config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        dataset = data_ingestion.get_data()
        dataset_pt = dataset.map(self.convert_examples_features, batched = True)
        ## Some of the systems may not have enough memory to train
        # so for such cases, we have to decrease the size of the dataset
        train = dataset_pt["train"]
        test = dataset_pt["test"]
        validation = dataset_pt["validation"]

        dataset_pt["train"] = train.select(range(int(train.num_rows * self.train_size)))
        dataset_pt["test"] = dataset_pt["test"].select(range(int(test.num_rows * self.test_size)))
        dataset_pt["validation"] = dataset_pt["validation"].select(range(int(validation.num_rows * self.validation_size)))
        return dataset_pt