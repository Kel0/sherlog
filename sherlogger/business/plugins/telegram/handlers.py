from inspect import getframeinfo, stack

from sherlogger.business.handlers import AbstractHandler
from sherlogger.business.models import BColors, LoggingLevel
from sherlogger.business.plugins.config import TelegramHandlerConfig
from sherlogger.business.utils import TGWriter
from sherlogger.logger import Logger


class TelegramHandler(AbstractHandler):
    def __init__(self, logger: Logger):
        super().__init__()

        # Define logger
        self._logger = logger

        # Load configs of telegram bot
        self.config = TelegramHandlerConfig(handler=self).load_from_config(
            path=self._logger.config.plugins_ini_path
        )
        self.writer = TGWriter(
            filename=self._logger.file_name,
            formatter=self._logger.config.formatter,
            streams=self.config.streams,
            chat_ids=self.config.chat_ids,
        )

    def _send(self, msg, level, color):
        caller = getframeinfo(stack()[-1][0])
        self.writer.post(msg=msg, level=level, color=color, lineno=caller.lineno)

    def info(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.INFO.value[0]:
            return

        self._send(msg=msg, level=LoggingLevel.INFO, color=BColors.OKBLUE.value)

    def debug(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.DEBUG.value[0]:
            return

        self._send(msg=msg, level=LoggingLevel.DEBUG, color=BColors.OKCYAN.value)

    def warning(self, msg) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.WARNING.value[0]:
            return

        self._send(msg=msg, level=LoggingLevel.WARNING, color=BColors.WARNING.value)

    def error(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.ERROR.value[0]:
            return

        self._send(msg=msg, level=LoggingLevel.ERROR, color=BColors.FAIL.value)

    def critical(self, msg: str) -> None:
        if self._logger.config.level.value[0] > LoggingLevel.CRITICAL.value[0]:
            return

        self._send(msg=msg, level=LoggingLevel.CRITICAL, color=BColors.FAIL.value)
