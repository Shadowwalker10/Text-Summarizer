from dataclasses import dataclass
from datasets import load_dataset
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    data_to_load: str