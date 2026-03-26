import socket

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 8888

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.bind((PROXY_HOST, PROXY_PORT))
proxy.listen(1)

print("🧠 Proxy running on port 8888...")

client_conn, client_addr = proxy.accept()
print("Client connected:", client_addr)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER_HOST, SERVER_PORT))

while True:
    data = client_conn.recv(1024)
    if not data:
        break

    print("\n🔍 Intercepted packet:", data.decode())

    # ✏️ MODIFY DATA (experiment here)
    modified_data = data.replace(b"move", b"jump")

    print("✏️ Modified packet:", modified_data.decode())

    # send to server
    server.send(modified_data)

    # get response from server
    response = server.recv(1024)

    print("📦 Server response:", response.decode())

    # send back to client
    client_conn.send(response)

client_conn.close()
server.close()
