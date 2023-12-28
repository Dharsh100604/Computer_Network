import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('127.0.0.1', 8000)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening on port 8000...")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Handle the client request
    data = client_socket.recv(1024).decode()
    if data == "80":
        response = "HTTP"
    elif data == "53":
        response = "DNS"
    elif data == "67":
        response = "DHCP SERVER"
    elif data == "21":
        response = "FTP"
    elif data == "68":
        response = "DHCP CLIENT"
    elif data == "25":
        response = "SMTP"
    elif data == "110":
        response = "POP3"
    elif data == "143":
        response = "IMAP4"
    elif data == "443":
        response = "HTTPS"
    elif data == "23":
        response = "TELNET"
    elif data == "22":
        response = "SSH"
    elif data == "179":
        response = "BGP"
    
    else:
        response = "Invalid request."

    # Send the response back to the client
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()