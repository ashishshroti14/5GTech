import socket
import threading
from device_manager import DeviceManager

class TCPServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.device_manager = DeviceManager()

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)
        print(f"Server started on {self.ip}:{self.port}")

        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                response = self.device_manager.process_request(data)
                client_socket.send(response)
            except ConnectionResetError:
                break
        client_socket.close()

if __name__ == "__main__":
    server = TCPServer("127.0.0.1", 65432)
    server.start_server()
