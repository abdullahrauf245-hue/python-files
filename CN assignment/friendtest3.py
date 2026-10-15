"""
EE-347 Computer Networks - Assignment 1
TCP Client

Asks the user for name and roll number, sends them to the server,
then waits for the server's reply and prints it.
"""

import socket

SERVER_PORT = 5000   # must match the server's port
BUFFER_SIZE = 1024
TIMEOUT_SECONDS = 10


def main():
    server_ip = input("Enter server IP: ").strip()
    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()

    if not server_ip or not name or not roll:
        print("[ERROR] Server IP, name and roll number cannot be empty.")
        return

    # Create a TCP/IPv4 socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(TIMEOUT_SECONDS)

    try:
        client_socket.connect((server_ip, SERVER_PORT))

        # Show this machine's details so screenshots can be told apart
        my_ip, my_port = client_socket.getsockname()
        print(f"\nConnected from {socket.gethostname()} ({my_ip}:{my_port})")

        # Send "name|roll_number" to the server
        client_socket.sendall(f"{name}|{roll}".encode("utf-8"))

        # Wait for and print the reply
        reply = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print("\nServer says:")
        print(reply)

    except socket.timeout:
        print("[ERROR] Connection timed out. Check the IP, network and server firewall.")
    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Is the server running on that IP and port?")
    except OSError as e:
        print(f"[ERROR] Network error: {e}")
    finally:
        client_socket.close()

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
