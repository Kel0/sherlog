from inspect import getmodule, stack

from .business.handlers import FileSystemHandler
from .business.plugins.telegram.handlers import TelegramHandler
from .logger import LoggerConfig, get_logger

_frame = stack()[-1]
_module = getmodule(_frame[0])

_module_name = "__main__"
if _module is not None:
    _module_name = _module.__file__.split("/")[-1]


logger = get_logger(_module_name)
logger.basic_config(handlers=[FileSystemHandler], level="INFO")


__all__ = [
    "logger",
    "get_logger",
    "LoggerConfig",
    "FileSystemHandler",
    "TelegramHandler",
]
