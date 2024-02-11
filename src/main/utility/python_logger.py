import logging
from logging.handlers import RotatingFileHandler
import os 

# Specify the absolute path for the log file
log_file_path = os.environ.get('log_file')

# Configure logging to write to a rotating file with a maximum size of 1 MB and keep up to 3 backup log files
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = RotatingFileHandler(log_file_path, maxBytes=1e6, backupCount=3)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_formatter)

# Also, configure logging to write to the console with a higher level (e.g., INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(log_formatter)

# Get the root logger and add the handlers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
