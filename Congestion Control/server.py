import time
import socket

def start_server():
    host = 'localhost'
    port = 12345

    # Create TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # Receive the data from client
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")

            # Simulate some processing time
            time.sleep(1)

            # Send acknowledgment
            client_socket.send(b"ACK")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Ensure the socket is properly closed
            client_socket.close()

if __name__ == "__main__":
    start_server()
