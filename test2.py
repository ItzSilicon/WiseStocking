import functions
from functions import log
import sys

logger=log()

def main():
    try:
        setting=functions.load_data_config()
    except Exception as msg:
        logger.error(msg)
        sys.exit(1)
    
main()