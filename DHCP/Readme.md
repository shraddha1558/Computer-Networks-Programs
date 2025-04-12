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


## One-Liners: 

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
