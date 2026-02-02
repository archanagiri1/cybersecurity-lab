import socket  # Used for network connections

# Take target IP address from user
target = input("Enter target IP address: ")

print(f"\nScanning target: {target}\n")

# Scan ports from 20 to 100
for port in range(20, 101):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout so scan doesn't hang
        s.settimeout(0.5)

        # Try connecting to the target and port
        result = s.connect_ex((target, port))

        # If connection is successful, port is open
        if result == 0:
            print(f"[+] Port {port} is OPEN")

        # Close the socket
        s.close()

    # Stop scan safely if user presses Ctrl+C
    except KeyboardInterrupt:
        print("\nScan stopped by user")
        break

    # Handle invalid hostname or IP
    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    # Handle connection errors
    except socket.error:
        print("Couldn't connect to server")
        break
