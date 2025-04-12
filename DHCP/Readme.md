# Manual DHCP Server-Client Simulation using UDP in Python

This is a **manual simulation** of the **DHCP (Dynamic Host Configuration Protocol)** using Python's `socket` library. It consists of two scripts:

- `dhcp_server.py` — Simulates a DHCP server
- `dhcp_client.py` — Simulates a DHCP client

The code uses **UDP sockets** to mimic the four-step DHCP handshake:
1. `DHCPDISCOVER` — Client requests an IP
2. `DHCPOFFER` — Server offers an IP
3. `DHCPREQUEST` — Client requests the offered IP
4. `DHCPACK` — Server confirms IP allocation

---

##  How to Run

### 1. Start the Server
```bash
python dhcp_server.py
```

### 2. Start the Client
```bash
python dhcp_client.py
```
## One-Liners: Question on given codes.

| Question                          | Answer                                                        |
|----------------------------------|---------------------------------------------------------------|
| What protocol is used?           | UDP (`socket.SOCK_DGRAM`)                                     |
| Can TCP be used?                 | No, DHCP needs UDP for broadcast and stateless setup         |
| What does 127.0.0.1 mean?        | Loopback IP (localhost, same machine)                         |
| Can I test this over LAN?        | Yes, change `SERVER_IP` to your local IP (e.g., `192.168.x.x`)|
| Can I assign real IPs?           | Not directly; this is just a simulation                       |
| What is port 6767?               | Custom port; changeable if needed                             |
| Can this assign IP to devices?   | No, it's a manual simulation for learning only                |
| What's the purpose of sleep(1)?  | Simulates delay before DHCPREQUEST                            |
| Why use `settimeout(10)`?        | So the server/client doesn't hang forever                     |
| Can this be extended?            | Yes, add features like IP release, renewal, lease timers etc. |


## Brief Introduction : Concept

Dynamic Host Configuration Protocol (DHCP) is an **application-layer protocol** based on the **client-server paradigm**, designed to assist the **TCP/IP protocol suite at the network layer**.

It automates the assignment of IP addresses and essential network parameters, making it a widely adopted **plug-and-play protocol** in modern networks.

### Key Functions of DHCP:
- **Permanent IP Assignment:** Network managers can assign static IPs to specific devices like routers or servers.
- **Temporary IP Assignment:** Enables devices (e.g., a traveler’s laptop in a hotel) to obtain an IP dynamically for a limited time.
- **Efficient IP Utilization:** ISPs can provide services to more households than available IPs by dynamically allocating IPs based on demand (e.g., 1000 IPs serving 4000 customers with non-overlapping usage).

### Essential Information Provided by DHCP:
To operate in a network, a host typically needs:
- **IP Address**
- **Subnet Mask (Network Prefix)**
- **Default Router (Gateway) Address**
- **DNS Server Address**

DHCP simplifies this configuration by automatically providing all four values to the host.

### Protocol Mechanics:
- DHCP uses **UDP** and operates on two well-known ports:
  - **Port 67** (Server)
  - **Port 68** (Client)
- Both ports are fixed, as the client receives **broadcasted replies** from the server. Since broadcast messages are not forwarded across routers, they are delivered to **all hosts within the same network**.

##  In Real Networks

- DHCP servers are usually built into **routers or switches**
- DHCP clients (devices) **broadcast** DHCPDISCOVER on the network to find a DHCP server
- Real IP configuration is handled by **OS-level network interfaces** and **network drivers**
- DHCP servers assign IPs from a **configured pool**, maintain **lease times**, and manage **conflicts**


> This Python script **simulates** the DHCP message exchange (DISCOVER → OFFER → REQUEST → ACK)  
> It does **not** alter your device’s actual network configuration — no real IP is assigned to any adapter


### Key Differences:
| Aspect                    | Real DHCP                            | This Script Simulation            |
|--------------------------|--------------------------------------|-----------------------------------|
| Protocol                 | UDP, Port 67 (server), 68 (client)   | UDP, custom port (6767)           |
| Broadcast support        | Full broadcast on local network      | Localhost only (`127.0.0.1`)      |
| IP assignment            | Real device network configuration    | Only prints/logs assigned IP      |
| Network impact           | Changes device's IP address          | No real changes on device         |
| Use case                 | Real-time networking                 | Educational & conceptual demo     |




> 📚 *Reference: Behrouz A. Forouzan, "Data Communications and Networking", 5th Edition, Chapter 23 - Dynamic Host Configuration Protocol (DHCP)*

