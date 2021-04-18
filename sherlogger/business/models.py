from dataclasses import dataclass
from enum import Enum


@dataclass
class WriteFormat:
    FORMAT = "{asctime} - {filename}:{lineno} - {levelname} - {message}"


class BColors(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class LoggingLevel(Enum):
    CRITICAL = (50, "CRITICAL")
    ERROR = (40, "ERROR")
    WARNING = (30, "WARNING")
    INFO = (20, "INFO")
    DEBUG = (10, "DEBUG")
    NOTSET = (0, "NOTSET")
