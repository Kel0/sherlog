from typing import List, Type, TypeVar, Union

from .business.models import LoggingLevel, WriteFormat

T = TypeVar("T")


class LoggerConfig:
    level: LoggingLevel = LoggingLevel.NOTSET
    formatter: str = WriteFormat.FORMAT
    handlers: List[Type[T]] = []
    propagate: bool = False
    plugins_ini_path = None

    def set_handlers(self, handlers):
        self.handlers = handlers

    def set_level(self, level: Union[int, str]):
        if isinstance(level, str):
            self.level = getattr(LoggingLevel, level.upper())
        else:
            if level == 0:
                self.level = LoggingLevel.NOTSET
            elif level == 10:
                self.level = LoggingLevel.DEBUG
            elif level == 20:
                self.level = LoggingLevel.INFO
            elif level == 30:
                self.level = LoggingLevel.WARNING
            elif level == 40:
                self.level = LoggingLevel.ERROR
            elif level == 50:
                self.level = LoggingLevel.CRITICAL

    def set_format(self, format_: str):
        WriteFormat.FORMAT = format_
        self.formatter = WriteFormat.FORMAT
