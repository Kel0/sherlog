from abc import ABC, abstractmethod
from inspect import getframeinfo, stack

from sherlogger.logger import Logger

from .config import HandlerConfig
from .models import BColors, LoggingLevel
from .utils import FSWriter


class AbstractHandler(ABC):
    def __init__(self):
        self.config = HandlerConfig(handler=self)
        self.writer = FSWriter(streams=self.config.streams, filename="", formatter="")

    @abstractmethod
    def info(self, msg: str) -> None:
        pass

    @abstractmethod
    def debug(self, msg: str) -> None:
        pass

    @abstractmethod
    def warning(self, msg: str) -> None:
        pass

    @abstractmethod
    def error(self, msg: str) -> None:
        pass

    @abstractmethod
    def critical(self, msg: str) -> None:
        pass


class FileSystemHandler(AbstractHandler):
    def __init__(self, logger: Logger) -> None:
        super().__init__()
        self._logger = logger
        self._build()

    def _build(self):
        self.writer.streams = self.config.streams
        self.writer.filename = self._logger.file_name
        self.writer.msg_format = self._logger.config.formatter

    def _post(self, msg, color, level):
        self._build()  # Check for paths and other stuff before processing the message
        caller = getframeinfo(stack()[-1][0])
        self.writer.write(msg=msg, lineno=caller.lineno, color=color, level=level)

    def info(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.INFO.value[0]:
            return

        self._post(msg=msg, color=BColors.OKBLUE, level=LoggingLevel.INFO)

    def debug(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.DEBUG.value[0]:
            return

        self._post(msg=msg, color=BColors.OKCYAN, level=LoggingLevel.DEBUG)

    def warning(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.WARNING.value[0]:
            return

        self._post(msg=msg, color=BColors.WARNING, level=LoggingLevel.WARNING)

    def error(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.ERROR.value[0]:
            return

        self._post(msg=msg, color=BColors.FAIL, level=LoggingLevel.ERROR)

    def critical(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.CRITICAL.value[0]:
            return

        self._post(msg=msg, color=BColors.FAIL, level=LoggingLevel.CRITICAL)
