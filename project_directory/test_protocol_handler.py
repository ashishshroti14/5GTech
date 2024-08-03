import unittest
from protocol_handler import protocol_handler
from device_manager import DeviceManager

class TestProtocolHandler(unittest.TestCase):
    def test_example_protocol(self):
        response = protocol_handler.handle_request("example", b"Test")
        self.assertEqual(response, b"Handled by example protocol")

class TestDeviceManager(unittest.TestCase):
    def test_process_request(self):
        device_manager = DeviceManager()
        response = device_manager.process_request(b"Test message")
        self.assertEqual(response, b"Handled by example protocol")

if __name__ == "__main__":
    unittest.main()
