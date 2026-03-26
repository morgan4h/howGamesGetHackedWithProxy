import socket
import time

HOST = "127.0.0.1"
PORT = 8888  # connect to proxy, NOT server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

actions = [
    "move_forward",
    "move_left",
    "attack",
    "move_backward"
]

for action in actions:
    print("🎮 Sending:", action)

    client.send(action.encode())

    response = client.recv(1024)
    print("📨 Response:", response.decode())

    time.sleep(1)

client.close()
