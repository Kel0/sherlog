# sherlog

Make `file system/network` logging stupid simple.


# Installation
```shell
pip install sherlogger
```

# Usage

### Default logger
By default, logger will record everything in the directory
where you calling it
```python
from sherlogger import logger


logger.info("Service is up...")
```
To change logs directory call `.set_streams()` method
```python
from sherlogger import logger
from sherlogger import FileSystemHandler


logger.set_streams(  # [<path_to_dirs>], <Handler>
    ["~/home/ubuntu/..."], FileSystemHandler
)
logger.info("THIS IS LOG MESSAGE")
```

### Telegram logger

#### Setup
* **.ini file**
    
    Create plugins.ini file. Format of file and required
    data is located in plugins.ini.example

Logger sends your message to telegram in asynchronous manner.

`telegram_logger` will send messages in separated thread.


### Custom logger
* **Import `get_logger` & handlers**
```python
from pathlib import Path

from sherlogger import get_logger, TelegramHandler, FileSystemHandler


ABS_PATH = Path().resolve()

logger = get_logger(__name__)
logger.basic_config(
  handlers=[TelegramHandler, FileSystemHandler],
  plugins_ini_path=f"{ABS_PATH}/plugins.ini",
  level="INFO"
)
logger.set_streams(
  ["./logs/"], FileSystemHandler
)
logger.info("This is a message")
```