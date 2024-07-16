import socket

# Define the host and port on which the server will listen
HOST = '127.0.0.1'  # Loopback address means localhost
PORT = 12345  # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind to the address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")
    
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    
    with client_socket:
        print(f"Connected by {client_address}")
        
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Print received data
            print(f"Received from client: {data.decode('utf-8')}")
            
            # Send a response back to the client
            client_socket.sendall(b"Message received. Thanks!")