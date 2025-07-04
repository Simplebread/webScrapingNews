# ========================================================================================
# error_log.py
#
# FILE OVERVIEW:
# This is a crucial utility module for the entire project. Its single purpose is
# to create and configure a standardized logger. Any other file in the project
# can call the `setup_logger` function to get a logger that behaves consistently
# ========================================================================================

# Import necessary libraries
import logging
from datetime import datetime

# Create reusable logger function
def setup_logger(name=None, log_file=None, level=logging.DEBUG):
    """
    Sets up a logger that writes to both the console and a file.
    It automatically creates the log directory if it doesn't exist and prevents
    the creation of duplicate log handlers.
    """
    # Create variables
    name = __name__
    log_file = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    # Create logger with name
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if already attached
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        ))

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        ))

        # Adding the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
