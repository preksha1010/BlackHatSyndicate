import socket

# Define the server's address and port
SERVER_HOST = '127.0.0.1'  # Server's loopback address
SERVER_PORT = 12345  # Port server is listening on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode('utf-8'))
    
    # Receive response from the server
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode('utf-8')}")