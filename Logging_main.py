# Logging Module

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %H:%M:%S')
import Logging_helper
""" logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a Warning message")    # Default
logging.error("This is a Error message")        # Default
logging.critical("This is a Critical message")  # Default """

logger = logging.getLogger(__name__)

# Create Handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and the Format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a Warning")
logger.error("This is a Error")


