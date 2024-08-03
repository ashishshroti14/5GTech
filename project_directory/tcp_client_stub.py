import socket

def tcp_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.send(b"Test message")
    response = client.recv(4096)
    print(response)
    client.close()

if __name__ == "__main__":
    tcp_client("127.0.0.1", 65432)
