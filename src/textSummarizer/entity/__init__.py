from dataclasses import dataclass
from datasets import load_dataset
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_to_load: str

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    tokenizer_name:Path
    train_size: float
    test_size:float
    validation_size:float
    input_encoding_length: int
    target_encoding_length: int


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    model_ckpt: Path
    num_train_epochs:int
    warmup_steps:int
    per_device_train_batch_size:int
    per_device_eval_batch_size:int
    weight_decay:float
    logging_steps:int
    evaluation_strategy:str
    eval_steps:int
    save_steps:int
    gradient_accumulation_steps:int
    gradient_checkpointing:bool
    fp16:bool


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    tokenizer_path: Path
    metrics_file_name: Path
