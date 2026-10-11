import socket

SERVER_IP = "10.202.41.238"   
PORT = 5000

def main():
    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()

    if not name or not roll:
        print("Name and roll number cannot be empty.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(10)   # don't hang forever if server is unreachable

    try:
        client.connect((SERVER_IP, PORT))
        client.sendall(f"{name}|{roll}".encode())

        reply = client.recv(1024).decode()
        print("\nServer says:")
        print(reply)

    except socket.timeout:
        print("Connection timed out. Check IP, network and firewall.")
    except ConnectionRefusedError:
        print("Connection refused. Is the server running?")
    except OSError as e:
        print(f"Network error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()