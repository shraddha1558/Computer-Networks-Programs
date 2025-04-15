import socket

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set DSCP in ToS field (e.g., Expedited Forwarding = 0xB8)
s.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 0xB8)

# Connect to local server on port 8080
s.connect(('localhost', 8086))

# Send basic HTTP GET request
s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

# Receive and print response
response = s.recv(4096)
print(response.decode())

s.close()
