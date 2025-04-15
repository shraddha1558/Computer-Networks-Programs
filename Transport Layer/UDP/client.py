import socket
import time

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Add delay before sending the message to simulate real-world behavior
time.sleep(2)  # Simulate delay before sending the message

# Send a message to the server (UDP does not require a connection)
message = b'Hello Server, This is the UDP client!'
client_socket.sendto(message, ('localhost', 12345))
print("Message sent to the server.")

# UDP does not wait for acknowledgment or response from the server.
# The client will just continue without waiting for any response.

# Close the socket after sending the message
client_socket.close()
print("Client socket closed.")
