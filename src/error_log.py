# Import necessary libraries
import logging

# Create reusable logger function
def setup_logger(name=None, log_file=None, level=logging.DEBUG):
    # Create variables
    name = __name__
    log_file = f"logs/{name}.log"

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

        # Console handler (optional)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "[%(levelname)s] %(message)s"
        ))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger