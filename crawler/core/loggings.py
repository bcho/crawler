# coding: utf-8

import logging
from logging import Formatter, FileHandler, StreamHandler


APP_LOGGER_NAME = 'crawler'


def file_handler_factory(fname, formatter):
    handler = FileHandler(fname)
    handler.setFormatter(formatter)

    return handler


def stream_handler_factory(formatter):
    handler = StreamHandler()
    handler.setFormatter(formatter)

    return handler


def setup_app_logger(handlers):
    logger = logging.getLogger(APP_LOGGER_NAME)
    logger.handlers = []
    logger.setLevel(logging.DEBUG)

    for handler in handlers:
        logger.addHandler(handler)

    return logger


def configure(config):
    formatter = Formatter(config['LOGGING_FORMAT'])
    file_handler = file_handler_factory(config['LOGGING_FILE'], formatter)
    stream_handler = stream_handler_factory(formatter)

    handlers = [file_handler, stream_handler]

    setup_app_logger(handlers)


logger = logging.getLogger(APP_LOGGER_NAME)
