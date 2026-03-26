import socket

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("🎮 Game Server running on port 9999...")

conn, addr = server.accept()
print("Connected by:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    print("📥 Server received:", data.decode())

    # respond to client
    response = f"Server got: {data.decode()}"
    conn.send(response.encode())

conn.close()
