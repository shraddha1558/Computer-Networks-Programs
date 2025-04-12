# NAT Simulation in Python

This repository contains Python code simulating the three types of Network Address Translation (NAT):  
**Static NAT**, **Dynamic NAT**, and **Port Address Translation (PAT)**.  
These NAT types are crucial in network management, allowing private IP addresses in a local network to communicate with external servers using a limited number of public IP addresses.

---

## Project Overview

This project demonstrates the working of three types of NAT through a simple simulation:

- **Static NAT** (One-to-One Mapping)
- **Dynamic NAT** (Many-to-Many Mapping)
- **Port Address Translation (PAT)** (Overloading)

Each type of NAT translates private IPs to public IPs differently, essential for managing limited public IPs in large networks.

---

## File Structure

```bash

NAT/
│
├── Static NAT.py # Static NAT Simulation
├── Dynamic NAT.py # Dynamic NAT Simulation
├── PAT NAT Overload.py # PAT (Port Address Translation) Simulation
└── README.md # Project Overview and Explanation


```
## Types of NAT Simulation

### 1. Static NAT (One-to-One Mapping)

- A private IP is always mapped to the same public IP.
- The mapping is **fixed** and does not change with each session.
- Suitable for devices that need consistent public accessibility (e.g., servers).

### 2. Dynamic NAT (Many-to-Many Mapping)

- Multiple private IPs are mapped to a **pool** of public IP addresses.
- The mappings are **temporary**, created as needed and deleted when the session ends.
- If all public IPs are in use, new connections are dropped.

### 3. Port Address Translation (PAT - Overloading)

- Multiple private IPs share a **single public IP**, differentiated by **port numbers**.
- PAT keeps track of each session using the source port, destination port, and IP addresses.
- Most commonly used form of NAT in home routers and corporate firewalls.

---

## Explanation of the Simulation

The simulation is written in Python and mimics how NAT works in real networks. Each NAT type uses a different logic:

### Static NAT:

- Implemented using a Python dictionary `static_nat_mapping`.
- Each private IP is assigned a fixed public IP.
- Repeated requests from the same private IP will always map to the same public IP.

### Dynamic NAT:

- A list of available public IPs (`public_ip_pool`) is maintained.
- When a private IP initiates a session, it is assigned an available public IP from the pool.
- If the pool is exhausted, further requests are denied (`"No available public IP"`).

### PAT:

- All private IPs are assigned the **same** public IP (`203.0.113.5`) but with **different ports**.
- Each private IP is assigned a unique port number starting from 10001.
- Mapping is stored in `pat_mapping` as a tuple of (public_ip, port).

---

## Conclusion

This project provides a basic simulation of the core NAT mechanisms used in networking:

- **Static NAT** for fixed one-to-one mapping.
- **Dynamic NAT** for flexible, temporary many-to-many mapping.
- **PAT** for efficient many-to-one mapping with port-based session tracking.

These concepts are foundational in understanding internet connectivity and IP management in routers and firewalls.

---

## Reference

- Behrouz A. Forouzan, _Data Communications and Networking_, McGraw-Hill Education.
