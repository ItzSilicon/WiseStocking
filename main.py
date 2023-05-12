from functions import log
global logger
logger=log()
try:
    import functions
    import sys
except Exception as msg:
    logger.error(msg)
    sys.exit(1)



def load_config():
    try:
        setting=functions.load_data_config()
    except Exception as msg:
        logger.error(msg)
        sys.exit(1)
    return setting
    