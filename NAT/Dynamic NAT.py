# Dynamic NAT Example

# Define the pool of public IPs
public_ip_pool = ["203.0.113.5", "203.0.113.6"]
private_ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40"]

# Function to assign public IP from the pool to private IP
def dynamic_nat(private_ip):
    if private_ip not in dynamic_nat_mapping:
        if len(dynamic_nat_mapping) < len(public_ip_pool):
            # Assign available public IP to private IP
            public_ip = public_ip_pool[len(dynamic_nat_mapping)]
            dynamic_nat_mapping[private_ip] = public_ip
        else:
            return "No available public IP"
    return dynamic_nat_mapping[private_ip]

# Create a dynamic NAT mapping dictionary
dynamic_nat_mapping = {}

# Test the function with multiple private IPs
for private_ip in private_ips:
    print(f"Private IP: {private_ip} -> Public IP: {dynamic_nat(private_ip)}")
