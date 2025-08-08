import logging

# Create logger
logger = logging.getLogger("my_logger")
if not logger.handlers:
    logger.setLevel(logging.DEBUG)

    # Create handler for console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    # Create handler for writing in a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
