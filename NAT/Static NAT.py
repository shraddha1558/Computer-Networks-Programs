# Static NAT Example

# Define the static NAT mapping (private IP to public IP)
static_nat_mapping = {
    "192.168.1.10": "203.0.113.5",
    "192.168.1.20": "203.0.113.6"
}

# Function to translate private IP to public IP
def static_nat(private_ip):
    public_ip = static_nat_mapping.get(private_ip, None)
    if public_ip:
        return public_ip
    else:
        return "No mapping found"

# Test the function
private_ip1 = "192.168.1.10"
private_ip2 = "192.168.1.25"  # This IP is not in the mapping

print(f"Private IP: {private_ip1} -> Public IP: {static_nat(private_ip1)}")
print(f"Private IP: {private_ip2} -> Public IP: {static_nat(private_ip2)}")
