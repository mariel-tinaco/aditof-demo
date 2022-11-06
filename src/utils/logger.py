"""
Loggers for Theia Framework

Copyright (c) 2022 Analog Devices, Inc. All Rights Reserved.
This software is proprietary and confidential to Analog Devices, Inc. and its licensors.
Author: Mariel Tinaco <mariel.tinaco@analog.com>
"""

import logging
from abc import ABC
import sys, os
class Logger(ABC):
    ...


class SystemLogger(Logger):

    def __init__(self) -> None:
        
        self.logger = logging.getLogger(SystemLogger.__name__)
        self.logger.setLevel(logging.DEBUG)

    def setup(self, file):
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler(file)
        fileHandler.setLevel(logging.DEBUG)


        formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s')

        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)
        self.logger.addHandler(consoleHandler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
