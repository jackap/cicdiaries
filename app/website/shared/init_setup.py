import logging
from logging import Formatter, FileHandler
import os


def setup_logging(app):
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'output.log')
    file_handler = FileHandler(log_path)
    handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.addHandler(file_handler)
