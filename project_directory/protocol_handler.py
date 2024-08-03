class ProtocolHandler:
    def __init__(self):
        self.protocols = {}

    def register_protocol(self, protocol_name, handler):
        self.protocols[protocol_name] = handler

    def handle_request(self, protocol_name, data):
        if protocol_name in self.protocols:
            return self.protocols[protocol_name](data)
        else:
            return b"Unsupported protocol"

def example_protocol_handler(data):
    return b"Handled by example protocol"

protocol_handler = ProtocolHandler()
protocol_handler.register_protocol("example", example_protocol_handler)
