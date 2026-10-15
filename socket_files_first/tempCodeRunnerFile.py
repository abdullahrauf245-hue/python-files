import socket
import time
 
HOST = "127.0.0.1"
PORT = 5004
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Boundary demo server waiting...")
 
conn, addr = server_socket.accept()
conn.sendall(b"AAAA")        # three separate send() calls
conn.sendall(b"BBBB")
conn.sendall(b"CCCC")
time.sleep(1)                # keep the connection open for a moment
conn.close()
server_socket.close()