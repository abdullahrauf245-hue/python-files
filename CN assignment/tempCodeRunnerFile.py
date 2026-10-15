"""
client.py - TCP client for EE-347 Assignment 1 (Client/Server application using sockets)

The client asks the user for their name and roll number, connects to the server,
sends them, waits for the server's reply and prints it on the screen.

Usage:
    python client.py                      (asks for the server IP, uses port 5050)
    python client.py 192.168.1.10         (server IP given, port 5050)
    python client.py 192.168.1.10 6000    (server IP and port given)
"""

import socket
import sys

DEFAULT_PORT = 5050   # must match the port the server is listening on
BUFFER_SIZE = 1024    # bytes read per recv() call
TIMEOUT = 10          # seconds to wait before giving up on the server


def main():
    # Server address: from the command line, or ask the user
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
    else:
        server_ip = input("Enter server IP: ").strip()

    port = DEFAULT_PORT
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Port must be a number, e.g. python client.py 192.168.1.10 5050")
            return

    # 1. Get the user's details
    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()
    if not name or not roll:
        print("Name and roll number cannot be empty.")
        return

    # 2. Create a TCP socket (IPv4 + stream)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(TIMEOUT)

    try:
        # 3. Connect to the server
        client_socket.connect((server_ip, port))

        # 4. Send "name|roll number", ending with a newline so the server knows the message is complete
        client_socket.sendall(f"{name}|{roll}\n".encode("utf-8"))

        # 5. Receive the full reply (the server closes the connection when it is done)
        reply = b""
        while True:
            chunk = client_socket.recv(BUFFER_SIZE)
            if not chunk:
                break
            reply += chunk

        # 6. Print the server's message
        print("\nServer says:")
        print(reply.decode("utf-8"))

    except socket.timeout:
        print(f"No response from {server_ip}:{port} within {TIMEOUT} seconds.")
    except ConnectionRefusedError:
        print(f"Connection refused by {server_ip}:{port}. Is the server running?")
    except socket.gaierror:
        print(f"Invalid server address: {server_ip}")
    except OSError as e:
        print(f"Network error: {e}")
    finally:
        # 7. Close the connection
        client_socket.close()


if __name__ == "__main__":
    main()
