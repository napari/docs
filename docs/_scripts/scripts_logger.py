"""Create a logger for a directory of scripts to aid in debugging."""

import logging
import os
import sys


def setup_logger(script_name, log_directory="logs"):
    """Sets up a logger for a specific script.

    Args:
        script_name (str): The name of the script (e.g., "my_script.py").
        log_directory (str, optional): The directory to store log files. Defaults to "logs".

    Returns:
        logging.Logger: A configured logger instance.
    """
    # Create log directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Extract the script name without the extension
    script_name_no_ext = os.path.splitext(script_name)[0]

    # Create a logger
    logger = logging.getLogger(script_name_no_ext)
    logger.setLevel(logging.DEBUG)  # Set the minimum logging level

    # Create a file handler
    # log_file_path = os.path.join(log_directory, f"{script_name_no_ext}.log")
    # file_handler = logging.FileHandler(log_file_path)
    # file_handler.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # file_handler.setFormatter(formatter)
    handler.setFormatter(formatter)

    # Add the file handler to the logger
    # logger.addHandler(file_handler)
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    # Example usage within a script
    current_script_name = os.path.basename(__file__)
    # Get the name of the current script
    logger = setup_logger(current_script_name)

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
