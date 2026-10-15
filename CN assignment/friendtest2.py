"""
client.py - Simple TCP client (EE-347 Assignment 1)

Asks for name and roll number, sends them to the server,
and prints the server's reply.

Usage:  python client.py <server_ip>
        (if no IP is given, it will ask for one)
"""

import socket
import sys

PORT = 5050  # must match the server's port


def main():
    # Get the server IP from the command line or by prompting
    server_ip = sys.argv[1] if len(sys.argv) > 1 else input("Enter server IP: ").strip()

    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()

    if not name or not roll:
        print("[ERROR] Name and roll number cannot be empty.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # don't wait forever
            s.connect((server_ip, PORT))
            s.sendall(f"{name}|{roll}".encode("utf-8"))

            reply = s.recv(4096).decode("utf-8")
            print("\nServer says:")
            print(reply)
    except socket.timeout:
        print("[ERROR] Connection timed out. Check the IP, port and firewall.")
    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Is the server running?")
    except OSError as e:
        print(f"[ERROR] Network error: {e}")


if __name__ == "__main__":
    main()
