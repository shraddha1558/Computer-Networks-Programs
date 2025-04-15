import socket
import time

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Add a delay before trying to connect to simulate real-world behavior
time.sleep(2)  # Wait for server to be ready

# Connect to the server (this triggers the handshake)
client_socket.connect(('localhost', 12345))
print("Connection established with the server.")

# Add a delay before sending the message
time.sleep(2)  # Simulate delay before sending the message

# Send a message to the server
client_socket.sendall(b'Hello Server, This is client...!')
print("Message sent to server.")

# Add a delay to simulate waiting for the server's acknowledgment
time.sleep(2)  # Simulate delay in waiting for the acknowledgment

# Receive the server's acknowledgment
acknowledgment = client_socket.recv(1024)
print(f"Acknowledgment received from server: {acknowledgment.decode()}")

# Add a delay before waiting for the final response
time.sleep(2)  # Simulate delay before receiving the final response

# Receive the server's final response
response = client_socket.recv(1024)
print(f"Server response: {response.decode()}")

# Add a delay before closing the connection
time.sleep(2)  # Simulate delay before closing the connection

# Close the connection
client_socket.close()
print("Connection closed.")
