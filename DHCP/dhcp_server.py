import socket

# Server IP and Port (localhost and arbitrary port for demo)
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6767

# Simple IP Pool
ip_pool = ['192.168.1.10', '192.168.1.11', '192.168.1.12']
# Dictionary to keep track of which client got which IP
assigned = {}

# Create a UDP socket (DHCP uses UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set timeout for receiving data (10 seconds)
sock.settimeout(10)  

# Bind the server socket to localhost and port 6767
sock.bind((SERVER_IP, SERVER_PORT))

print(" DHCP Server running...")
# Start listening for DHCP messages from clients

while True:
    try:
        
        # Receive data from a client (buffer size is 1024 bytes)
        data, addr = sock.recvfrom(1024)
        print(f" Received data from {addr}: {data.decode()}")
        
        message = data.decode()
        
        # If the client is discovering available DHCP servers
        if message == "DHCPDISCOVER":
            print(f"[{addr}] ➜ DISCOVER received.")
            
            # If this client hasn't already been assigned an IP, pop the first IP from the pool and assign it
            if addr not in assigned:
                offered_ip = ip_pool.pop(0)
                assigned[addr] = offered_ip
                
                 # Send the offered IP to the client
                sock.sendto(f"DHCPOFFER:{offered_ip}".encode(), addr)
                print(f"Offered IP {offered_ip} to {addr}")
        
        
        # If the client is requesting the offered IP
        elif message.startswith("DHCPREQUEST:"):
            requested_ip = message.split(":")[1]
            
            # Confirm that the requested IP matches the one assigned
            if assigned[addr] == requested_ip:
                # Send acknowledgment to the client
                sock.sendto(f"DHCPACK:{requested_ip}".encode(), addr)
                print(f"ACK sent to {addr} for IP {requested_ip}")
                
    # If no message is received within timeout duration
    except socket.timeout:
        print(" Timeout: No message received. Server waiting...")
        break  # Stop the server loop after timeout
