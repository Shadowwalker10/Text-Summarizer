import torch
torch.cuda.empty_cache()
from transformers import pipeline
# from textSummarizer.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.config = self.config.get_model_evaluation_config() ##we are using model evalaution config since model and tokenizer paths are defined in it
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    def predict(self, text):
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        pipe = pipeline("summarization", 
                        model=self.config.model_path, 
                        tokenizer=self.config.tokenizer_path, device=self.device)
        summary = pipe(text, num_workers=-1, **gen_kwargs)[0]["summary_text"].replace("<n>", "")
        print("\nModel Summary:\n")
        print(summary)
        return summary


