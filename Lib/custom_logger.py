import logging


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
