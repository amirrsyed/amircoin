import socket
import threading

class NetworkNode:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.peers = []

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Server started at {self.host}:{self.port}")
        
        while True:
            client, addr = server.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            client_socket.send(data)
        client_socket.close()

    def connect_to_peer(self, peer_host, peer_port):
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_host, peer_port))
        self.peers.append(peer)
        threading.Thread(target=self.handle_peer, args=(peer,)).start()

    def handle_peer(self, peer_socket):
        while True:
            data = peer_socket.recv(1024)
            if not data:
                break
            print(f"Received from peer: {data.decode('utf-8')}")
            peer_socket.send(data)
        peer_socket.close()

    def broadcast(self, message):
        for peer in self.peers:
            peer.send(message.encode('utf-8'))
