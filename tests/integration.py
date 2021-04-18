from pathlib import Path

from sherlogger import get_logger, FileSystemHandler


ABS_PATH = Path().resolve().parent

logger = get_logger(__name__)
logger.basic_config(
    handlers=[FileSystemHandler],
    plugins_ini_path=f"{ABS_PATH}/plugins.ini",
    level="INFO",
)
logger.set_streams(
    [f"{ABS_PATH}/tests/logs/"], FileSystemHandler
)

logger.error("Something")
