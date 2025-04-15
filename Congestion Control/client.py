import socket
import time

def start_client():
    host = 'localhost'
    port = 12345
    congestion_window = 1  # Start with a small congestion window
    max_window_size = 10  # Max congestion window size
    round_trip_time = 0.1  # Simulated RTT (in seconds)

    # Create TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Disable Nagle’s Algorithm

    try:
        # Connect to the server
        print("Attempting to connect to server...")
        client_socket.connect((host, port))
        print("Connected to server!")

        message = "Hello, Server!"
        while congestion_window <= max_window_size:
            print(f"Sending message with congestion window size: {congestion_window}")

            # Send data to server
            client_socket.send(message.encode())

            # Wait for acknowledgment from server (simulated RTT)
            time.sleep(round_trip_time)

            # Simulate packet loss based on congestion window (simple approximation)
            if congestion_window >= 4:
                print("Simulating packet loss...")
                congestion_window //= 2  # Reduce the window size if packet loss occurs
            else:
                congestion_window += 1  # Increase the window size if no loss

            # Receive acknowledgment
            ack = client_socket.recv(1024)
            print(f"Received: {ack.decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket gracefully
        client_socket.close()

if __name__ == "__main__":
    start_client()
