import socket
 
HOST = "127.0.0.1"
PORT = 5000
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to TCP server.")
 
while True:
    message = input("Enter message: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    response = client_socket.recv(1024)
    print("Server:", response.decode())
 
client_socket.close()
print("Client closed.")