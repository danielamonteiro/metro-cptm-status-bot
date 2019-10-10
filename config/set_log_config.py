import logging
import os
import configparser
import errno
from logging.config import fileConfig


def check_config_file():
    base_path = os.path.abspath(os.path.dirname(__file__))
    log_file_config = base_path + "\logging.conf"
    config = configparser.ConfigParser()
    config.read(log_file_config)
    log_file_name = config.get('handler_file_handler', 'args')
    log_file_name = log_file_name.split(',')[0][1:].replace("'", "")
    try:
        fileConfig(log_file_config)
    except Exception as e:
        print("Invalid logging config file [" + log_file_config + "]")
        print(e)