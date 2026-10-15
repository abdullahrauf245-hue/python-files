import socket
import time
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5004))
time.sleep(0.5)              # let all three sends arrive first
 
data = client_socket.recv(1024)   # ONE recv() call
print("recv() returned:", data)
print("Number of bytes:", len(data))
client_socket.close()