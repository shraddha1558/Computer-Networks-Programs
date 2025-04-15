import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind(('localhost', 12345))
print("Server is listening for incoming messages...")

while True:
    # Receive message from the client (1024 bytes buffer size)
    data, addr = server_socket.recvfrom(1024)
    print(f"Received message: {data.decode()} from {addr}")
    # No acknowledgment is sent, the server just receives and prints the message
