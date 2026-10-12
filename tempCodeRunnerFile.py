import socket
from datetime import datetime
HOST = "0.0.0.0"   # listen on all network interfaces
PORT = 5000        # chosen port
def main():
    request_count = 0
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind((HOST, PORT))
        server.listen(5)
    except OSError as e:
        print(f"Could not start server: {e}")
        return
    print(f"Server listening on port {PORT}... (Ctrl+C to stop)")
    try:
        while True:
            conn, addr = server.accept()
            client_ip, client_port = addr
            with conn:
                try:
                    request_count += 1
                    data = conn.recv(1024).decode().strip()
                    name, roll = data.split("|", 1)
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    reply = (
                        f"Hello {name} ({roll})\n"
                        f"Your address: {client_ip}:{client_port}\n"
                        f"Request number: {request_count}\n"
                        f"Server date/time: {now}"
                    )
                    conn.sendall(reply.encode())

                    print(f"[Request #{request_count}] {name} ({roll}) "
                          f"from {client_ip}:{client_port} at {now}")
                except ValueError:
                    conn.sendall("Invalid data format.".encode())
                    print(f"Bad data received from {client_ip}:{client_port}")
                except (ConnectionResetError, BrokenPipeError):
                    print(f"Client {client_ip}:{client_port} disconnected early")
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()
if __name__ == "__main__":
    main()