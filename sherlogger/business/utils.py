import asyncio
from datetime import datetime

import aiohttp

from .models import BColors, LoggingLevel
from .plugins.telegram.executor import run_in_separated_thread


class Writer:
    """
    Write provided messages to file
    """

    def __init__(self, filename: str, formatter: str, streams: list, chat_ids=None):
        self.chat_ids = chat_ids
        if self.chat_ids is None:
            self.chat_ids = []

        self.streams = streams
        self.filename = filename
        self.msg_format = formatter

    def create_message(self, msg: str, lineno: int, level):
        """
        Initialize message from provided inputs

        :param msg: Message text
        :param lineno: Line number where logger was called
        :param level: Level of logger
        """
        now_time = datetime.utcnow()

        return self.msg_format.format(
            asctime=now_time,
            filename=self.filename,
            lineno=lineno,
            levelname=level,
            message=msg,
        )


class FSWriter(Writer):
    def __init__(self, filename: str, formatter: str, streams: list):
        super().__init__(filename=filename, formatter=formatter, streams=streams)

    def write(self, msg: str, lineno: int, color, level):
        """
        Write message to file

        :param msg: Message text
        :param lineno: Line number where logger was called
        :param color: Color of print text
        :param level: Level of logger
        """
        message = self.create_message(msg=msg, lineno=lineno, level=level)

        if not self.streams:
            print(color.value + message + BColors.ENDC.value)
            return

        for stream in self.streams:
            self._pre_proc(
                msg=message, level=level, stream=stream
            )  # Check for logging levels
            with open(stream + level.value[1].lower() + ".log", "a+") as f:
                f.write(message + "\n")

        print(color.value + message + BColors.ENDC.value)

    def _pre_proc(self, msg, level, stream):
        """
        Check for level of logger, and write message to info.log if logger's level is not `INFO`

        :param msg: Message text
        :param level: Level of logger
        """
        if level.value[1] != "INFO":
            with open(stream + LoggingLevel.INFO.value[1].lower() + ".log", "a+") as f:
                f.write(msg + "\n")


class TGWriter(Writer):
    def __init__(self, filename: str, formatter: str, streams: list, *, chat_ids=None):
        super().__init__(
            filename=filename, formatter=formatter, streams=streams, chat_ids=chat_ids
        )

    async def _post(self, msg):
        for token in self.streams:
            for chat_id in self.chat_ids:

                payload = {"chat_id": chat_id, "text": msg, "parse_mode": "HTML"}
                url = "https://api.telegram.org/bot{api_token}/sendMessage".format(
                    api_token=token
                )

                async with aiohttp.ClientSession() as session:
                    async with session.post(url, data=payload) as _:
                        await asyncio.sleep(0)

    def post(self, msg: str, lineno: int, color, level):
        message = self.create_message(msg=msg, lineno=lineno, level=level)
        print(color + message + BColors.ENDC.value)
        run_in_separated_thread(self._post, message=message)
