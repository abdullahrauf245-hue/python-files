import socket
 
HOST = "127.0.0.1"
PORT = 5001
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print("UDP Server is waiting for messages...")
 
while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()
    print("Client:", message)
    if message.lower() == "exit":
        break
    response = "Server received: " + message
    server_socket.sendto(response.encode(), addr)
 
server_socket.close()
print("UDP Server closed.")