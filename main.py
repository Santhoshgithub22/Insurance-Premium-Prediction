from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
import os, sys

def test_logger_and_exception():
    try:
        logging.info("Starting the test and logger exception")
        result = 3/0
        print(result)
        logging.info("Ending point of the test and logger exception")

    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)
    
if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)