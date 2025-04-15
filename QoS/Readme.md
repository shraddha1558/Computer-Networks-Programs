# Understanding Quality of Service (QoS) in Networking

## What is QoS?

**Quality of Service (QoS)** is a technique used in computer networks to manage and control **network traffic**. It ensures certain types of data are delivered **faster, more reliably, and with better quality** than others.

### Why is QoS Important?

Imagine you're on a video call and also downloading a large file. QoS ensures the **video call (real-time data)** gets higher priority so it doesn’t lag, even if the file download is ongoing.

---

## How QoS Works

QoS works by **tagging** packets (units of data in a network) and **prioritizing** them based on their type and urgency.

- It operates mainly at:

  - **Network Layer (Layer 3)**: where IP addresses are handled.
  - **Transport Layer (Layer 4)**: where protocols like TCP/UDP operate.

- Packets are marked with special values (e.g., DSCP), which routers and switches read to decide which packets to process first.

---

## Key QoS Concepts (Simplified)

| Concept                   | What It Means                                                     |
| ------------------------- | ----------------------------------------------------------------- |
| **DSCP**                  | A code added to packets to indicate their priority level.         |
| **ToS (Type of Service)** | An older way to set priority in IP packets, now replaced by DSCP. |
| **Traffic Shaping**       | Slowing down packets to keep traffic smooth and within limits.    |
| **Traffic Policing**      | Cutting off or limiting traffic if it breaks the rules.           |
| **Priority Queuing**      | Higher priority traffic is put at the front of the line.          |

---

## Ways to Enable QoS

### 1. **Program Level**

- Software can mark outgoing packets with a priority value.
- For example, a video conferencing app can tag its traffic as "high priority" so the network knows to handle it faster.

### 2. **Operating System Level**

- OS-level tools can define rules for traffic control.
  - On **Linux**: `tc` (traffic control) can be used to shape and prioritize traffic.
  - On **Windows**: Group Policy Editor allows you to set QoS policies.

### 3. **Router/Switch Level**

- Network admins configure devices to recognize and act on QoS markings.
  - They can assign specific bandwidth, drop policies, and priority queues for different types of traffic.

### 4. **Cloud & WAN Services**

- Cloud providers like AWS, Azure, and GCP allow tagging packets for QoS within virtual networks.
- Some advanced SD-WAN and VPN solutions come with built-in QoS support.

---

## Real-World Example (Without Code)

Let’s say you open a video streaming app:

1. The app sets a DSCP value on its packets to request high priority.
2. Your router recognizes this tag and processes the video packets first.
3. If someone else on the network starts a big download, the router delays those packets slightly to keep your video smooth.

---

## Key Takeaways

- QoS ensures **critical or time-sensitive data** gets through the network smoothly.
- It's a collaborative effort: **Apps + OS + Network Devices** must all support QoS for it to work properly.
- QoS does **not increase bandwidth**, but it **manages how bandwidth is used**.

---

## 🎯 Purpose of the Code

This code demonstrates how to:

- **Establish a TCP connection**: It creates a connection with a local server running on port 8086. This is typically used for local testing purposes.
- **Tag packets for QoS (Quality of Service)**: It marks outgoing packets with a DSCP value of `0xB8` (Expedited Forwarding). This tag tells the network that these packets are important and should be processed first for better performance.
- **Send an HTTP GET request**: The code sends a simple HTTP GET request to the server to fetch data (like requesting a webpage).
- **Demonstrate QoS concept**: The code shows how applications can set packet priorities to manage network traffic effectively.

---

## ❌ Limitations

While this code demonstrates the QoS tagging, there are some limitations to keep in mind:

- **Does not guarantee QoS**: The code sets the DSCP tag, but your network hardware (like routers and switches) must support and respect DSCP tagging for QoS to actually happen. If the hardware ignores it, the packet prioritization won’t be effective.
- **Local server needed**: This code requires a local HTTP server running on port 8086. You can start a local server by using the command: `python -m http.server 8086`.
- **Only outgoing traffic is marked**: The DSCP tag is applied only to packets sent from your computer. How incoming packets are handled depends on the sender and their QoS settings.
- **Verification required**: You need to verify if the DSCP tag is applied correctly by using packet inspection tools like `tcpdump` or `Wireshark`.

---

## 🧪 How to Verify DSCP Tag

To check if the DSCP value was applied successfully to the packets:

1. Open your terminal.
2. Use the following command to monitor network traffic:

```bash
sudo tcpdump -i lo -v tcp port 8086
```

## ✅ DOs and ❌ DON'Ts

### DO ✅

- **Run the server before the client:** Make sure your HTTP server is running before you execute the client code.
- **Use loopback (localhost) for testing:** It's recommended to test with localhost (127.0.0.1) during development.
- **Use admin/sudo for tcpdump:** To capture network traffic on your system, ensure you have the necessary permissions (admin/sudo) for tcpdump.

### DON'T ❌

- **Assume routers honor DSCP by default:** Not all routers or network devices automatically prioritize packets based on DSCP. You'll need to configure them properly.
- **Skip packet inspection:** Don't skip verifying DSCP tags with tools like tcpdump or Wireshark. This helps ensure your QoS settings are working.
- **Forget to close the socket:** Always make sure to close the socket after the program runs to avoid network issues.

### 🧠 Beginner Tip

- **DSCP value may be ignored by some routers:** Even though the DSCP value is set in code, your home or college router might ignore it unless it is explicitly configured to honor QoS markings.
- **Verify with tools and network setup:** This code demonstrates the concept of QoS, but to see the actual impact, you need to verify it using packet inspection tools like tcpdump or Wireshark and ensure proper network configuration.
