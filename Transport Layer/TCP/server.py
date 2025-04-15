import socket
import time

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(('localhost', 12345))

# Start listening for incoming connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept a connection (this blocks until the client connects)
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Add a delay to simulate processing
time.sleep(2)  # Simulate processing time on server side

# Receive data from the client
data = conn.recv(1024)
print(f"Received request from client: {data.decode()}")

# Acknowledge the request from the client
conn.sendall(b'ACK: Request received')

# Add a delay before responding to the client
time.sleep(2)  # Simulate delay in processing the response

# Send a response back to the client
conn.sendall(b'Hello from Server!')

# Simulate some interaction (delay)
time.sleep(2)  # Simulate interaction delay

# Close the connection
conn.close()
print("Connection closed.")

# Close the server socket
server_socket.close()
print("Server socket closed.")
