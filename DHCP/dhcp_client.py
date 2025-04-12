import socket
import time

# Define the server's IP and port (localhost for testing)
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6767

# Create a UDP socket (DHCP uses UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set timeout for receiving data (10 seconds)
sock.settimeout(10)  

# 1. Send DHCPDISCOVER to server
print(" Sending DHCPDISCOVER...")
sock.sendto("DHCPDISCOVER".encode(), (SERVER_IP, SERVER_PORT))

# 2. Wait for DHCPOFFER from server
try:
    data, _ = sock.recvfrom(1024)
    offer = data.decode()
    
    # If received message is an IP offer
    if offer.startswith("DHCPOFFER:"):
        offered_ip = offer.split(":")[1]
        print(f" Received DHCPOFFER with IP: {offered_ip}")

        # 3. Send DHCPREQUEST for the offered IP
        time.sleep(1)
        sock.sendto(f"DHCPREQUEST:{offered_ip}".encode(), (SERVER_IP, SERVER_PORT))
        print(f" Sent DHCPREQUEST for IP: {offered_ip}")

        # 4. Wait for DHCPACK back from server
        data, _ = sock.recvfrom(1024)
        ack = data.decode()
        
        # If server confirms the IP assignment
        if ack.startswith("DHCPACK:"):
            confirmed_ip = ack.split(":")[1]
            print(f" Received DHCPACK. IP {confirmed_ip} assigned successfully!")
            
# If the server doesn't respond within 10 seconds
except socket.timeout:
    print("Timeout: No response from server.")
    exit()
