import os
import sys
import logging  ##with this we will be creating our custom logging

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

log_dir="logs"

log_filepath=os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Corrected class name
        logging.StreamHandler(sys.stdout)   # Corrected class name
    ]
)

logger=logging.getLogger("mlprojectlogger")