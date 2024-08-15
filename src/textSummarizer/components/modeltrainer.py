## Defining Components
## Datacollator helps to batch the data while feeding it to the model
from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
from textSummarizer.entity import ModelTrainerConfig
from datasets import load_dataset, load_from_disk
import torch


class ModelTrainer:
    def __init__(self, 
                 config: ModelTrainerConfig, 
                 dataset):
        self.config = config
        self.dataset = dataset
        # print(self.config)
        # print("*"*100)


    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(pretrained_model_name_or_path=self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model_pegasus)

        trainer_args = TrainingArguments(output_dir=self.config.root_dir,
                                         num_train_epochs=self.config.num_train_epochs,
                                         warmup_steps=self.config.warmup_steps,
                                         per_device_train_batch_size = self.config.per_device_train_batch_size,
                                         weight_decay=self.config.weight_decay,
                                         logging_steps=self.config.logging_steps,
                                         evaluation_strategy=self.config.evaluation_strategy,
                                         eval_steps=self.config.eval_steps,
                                         save_steps = self.config.save_steps,
                                         gradient_accumulation_steps = self.config.gradient_accumulation_steps,
                                         gradient_checkpointing = self.config.gradient_checkpointing,
                                         fp16 = self.config.fp16
                                         )
        


        trainer = Trainer(model=model_pegasus, 
                          args=trainer_args, 
                          data_collator=seq2seq_data_collator, 
                          train_dataset = self.dataset["test"],#change here if you have enough memory to change to train data
                          eval_dataset = self.dataset["validation"])
        
        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        ##Save the tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))







