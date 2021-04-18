from .business.models import LoggingLevel
from .config import LoggerConfig


def get_logger(filename) -> "Logger":
    return Logger(filename)


class Logger:
    config = LoggerConfig()

    def __init__(self, file_name: str):
        self.file_name = file_name

    def basic_config(self, **kwargs):
        for field, value in kwargs.items():
            if not hasattr(self.config, field.lower()):
                raise AttributeError(
                    "No {field} in config of logger.".format(field=field)
                )

            if field.lower() == "level":
                if not isinstance(value, str):
                    raise AttributeError("Level should be provided as a string.")

                value = getattr(LoggingLevel, value)

            setattr(self.config, field, value)

    def set_streams(self, streams: list, type_):
        for idx, handler in enumerate(self.check_handlers()):

            if not isinstance(handler, type_):
                continue

            handler.config.set_stream_chain(
                streams=streams,
            )

    def check_handlers(self):
        for idx, handler in enumerate(self.config.handlers):
            if callable(handler):
                handler = handler(logger=self)
                self.config.handlers[idx] = handler

            yield handler

    def info(self, msg):
        for handler in self.check_handlers():
            handler.info(msg=msg)

    def debug(self, msg):
        for handler in self.check_handlers():
            handler.debug(msg=msg)

    def warning(self, msg):
        for handler in self.check_handlers():
            handler.warning(msg=msg)

    def error(self, msg):
        for handler in self.check_handlers():
            handler.error(msg=msg)

    def critical(self, msg):
        for handler in self.check_handlers():
            handler.critical(msg=msg)
