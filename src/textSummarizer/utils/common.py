import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

"""
1) 
In dictionaries, it's not possible to access the value using the key using this method:
d = {"key": "value"}
d.key::: This gives error

So, to make it possibe:
we pass the dictionary to ConfigBox
d = ConfigBox({"key": "value"})
d.key
Now it works and returns value
"""

"""
2) 

Use of ensure_annotations

suppose, my function is:
def get_prod(x:int, y:int)->int

If I give integers, it works fine but if I pass str, it still works

for example:
def get_prod(2, "4"):
This returns 44

So, to ensure that the annotations provided to the variables are satisifed, we use ensure annotations

@ensure_annotations
def get_prod(x:int, y:int)->int:
return x*y

get_prod(2, "4")---> This now throws an error
"""
@ensure_annotations
def read_yamp(path_to_yaml_file:Path)->ConfigBox:
    """
    Reads yaml file and return configbox object

    Args:
        path_to_yaml_file: Path to yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: Configbox type
    
    """

    try:
        with open(path_to_yaml_file, "rb") as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file {path_to_yaml_file} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories_and_files(lst_directories__files_path:list, verbose = True):
    """
    Creates parent directories and files if any

    Args:
        lst_directories_path: List of directories paths
    """
    directories = [str(Path(p)) for p in lst_directories__files_path]
    [os.makedirs(p, exist_ok = True) for p in directories]
    

    ## Creating files inside directories if any
    [Path(p).touch(exist_ok = True) for p in lst_directories__files_path]
    

    if verbose:
        logger.info(f"Parent Directories Created Successfully")
        logger.info("Files Inside Directories Created.")

@ensure_annotations
def get_size(path:Path)->str:
    """
    Returns size in kb

    Args:
        path (Path): path of the file
    
    Returns:
        str: size of the file in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"







