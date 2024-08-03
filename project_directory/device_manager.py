from protocol_handler import protocol_handler

class DeviceManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, device_id, protocol):
        self.devices[device_id] = protocol

    def process_request(self, data):
        # Example of processing data, you would parse the data to find the device_id and protocol
        device_id = "example_device_id"
        protocol_name = "example"
        response = protocol_handler.handle_request(protocol_name, data)
        return response
