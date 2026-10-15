# EE-347 Computer Networks - Assignment 1

import socket

PORT = 5000   # must match the server's port


def main():
    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()
    server_ip = input("Enter server IP: ").strip()

    if not name or not roll:
        print("Name and roll number cannot be empty.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect((server_ip, PORT))
            s.sendall(f"{name}|{roll}".encode())

            reply = s.recv(1024).decode()
            print("\nServer says:")
            print(reply)

    except socket.timeout:
        print("Error: connection timed out. Check the IP and the server's firewall.")
    except ConnectionRefusedError:
        print("Error: connection refused. Is the server running on that port?")
    except socket.gaierror:
        print("Error: invalid server address.")
    except OSError as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()