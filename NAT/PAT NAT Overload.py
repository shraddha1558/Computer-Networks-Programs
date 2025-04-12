# PAT (Port Address Translation) Example

# Define the public IP and starting port
public_ip = "203.0.113.5"
starting_port = 10001

# Dictionary to hold the mapping of private IP to (public IP, port)
pat_mapping = {}

# Function to assign public IP and port to private IP
def pat(private_ip):
    global starting_port
    if private_ip not in pat_mapping:
        pat_mapping[private_ip] = (public_ip, starting_port)
        starting_port += 1
    return pat_mapping[private_ip]

# Test the function with multiple private IPs
private_ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40"]

for private_ip in private_ips:
    public_ip, port = pat(private_ip)
    print(f"Private IP: {private_ip} -> Public IP: {public_ip}:{port}")
