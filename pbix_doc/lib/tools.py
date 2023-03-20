def setup_logger(log_file):
    import logging

    # Set up the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Set up a file handler to write to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Set up a stream handler to write to stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # Set the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
