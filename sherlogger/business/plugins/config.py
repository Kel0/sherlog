import configparser

from sherlogger.business.config import HandlerConfig


def _get_section_of_ini_safe(config):
    try:
        return config["tg_bot"]
    except KeyError:
        return None


class TelegramHandlerConfig(HandlerConfig):
    def __init__(self, handler):
        super().__init__(handler=handler)
        self.chat_ids = []

    def set_chat_ids(self, chat_ids: str):
        self.chat_ids += chat_ids.split(",")

    def set_stream_chain(self, streams: list):
        self.streams = streams

    def load_from_config(self, path: str):
        config = configparser.ConfigParser()
        config.read(path)
        tg_bot = _get_section_of_ini_safe(config)

        self.chat_ids = tg_bot["chat_ids"].split(",")
        self.streams = tg_bot["api_tokens"].split(",")

        return self
