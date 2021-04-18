class HandlerConfig:
    def __init__(self, handler):
        self.handler = handler
        self.streams = ["./"]
        self.filename = "Undefined"

    def set_stream_chain(self, streams: list):
        self.streams = streams
