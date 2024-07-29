import os
import sys
import logging
from pathlib import Path

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_filepath = "./logs/running_logs.log"

os.makedirs(str(Path(log_filepath).parent),exist_ok=True)

Path(log_filepath).touch(exist_ok = True)



logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")


