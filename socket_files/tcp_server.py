import socket
 
HOST = "127.0.0.1"
PORT = 5000
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("TCP Server is waiting for a connection...")
 
conn, addr = server_socket.accept()
print("Connected by:", addr)
 
while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print("Client:", message)
    if message.lower() == "exit":
        break
    response = "Server received: " + message
    conn.send(response.encode())
 
conn.close()
server_socket.close()
print("Server closed.")