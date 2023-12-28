import socket
import tkinter as tk
from tkinter import font

well_known_ports = {
    "HTTP": "Hypertext Transfer Protocol (HTTP) - Port 80: Used for serving web pages over the internet.",
    "HTTPS": "HTTP Secure (HTTPS) - Port 443: Used for secure web page serving over the internet.",
    "DNS": " Domain Name System (DNS)- Port 53 is used for DNS, which is responsible for translating\n human-readable domain names into IP address",
    "DHCP SERVER":"Dynamic Host Configuration Protocol (DHCP) Server-Port 67 is typically used by\n DHCP servers to dynamically assign IP addresses and network configuration settings to devices on a network.",
    "FTP":"File Transfer Protocol (FTP)-Port 21 is the default control port for FTP, \na standard network protocol used to transfer files between a client and a server over a network",
    "SMTP":"Simple Mail Transfer Protocol (SMTP)- Port 25 is used for SMTP, which is a \nprotocol for sending email messages between email servers.",
    "POP3":"Post Office Protocol version 3 (POP3)-Port 110 is used for POP3, a protocol \nfor retrieving email messages from a mail server. \nPOP3 allows email clients to download messages from the server and store them",
    "TELNET":"Telnet-Port 23 is used for Telnet, a network protocol that provides a virtual \nterminal connection to remote devices over a network",
    "SSH":"Secure Shell (SSH)-Port 22 is used for SSH, a secure network protocol for securely accessing \nand managing remote devices over a network. SSH provides encrypted communication",
    "IMAP4":"Internet Message Access Protocol (IMAP)-Port 143 is used for IMAP, which is an email \nretrieval and storage protocol. IMAP allows email clients to access and manage email messages stored on a remote email server",
    "BGP":"Border Gateway Protocol (BGP)-Port 179 is used for BGP, a standardized exterior gateway protocol used to \nexchange routing and reachability information between autonomous systems on the internet.",
}

def send_request_to_server():
    request = request_entry.get()

   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 8000)

    try:
        client_socket.connect(server_address)

        # Send the request to the server
        client_socket.send(request.encode())

        # Receive and print the server's response
        response = client_socket.recv(1024).decode()
        result_label.config(text=f"Server response: {response}")
        if response in well_known_ports:
            result_label.config(text=f"Server response: {response}\nPort Info: {well_known_ports[response]}\n")
    except ConnectionRefusedError:
        result_label.config(text="Server is not running or the connection was refused.")
    finally:
        # Close the client socket
        client_socket.close()

# Create the main window
root = tk.Tk()
root.title("Well Known port Info Service")
custom_font = font.Font(family="Helvetica", size=16)
frame = tk.Frame(root, width=150, height=400)
frame.pack()

title_label = tk.Label(frame, text="Well Known Port Info Service", font=custom_font)
title_label.pack()

# Create and configure widgets
request_label = tk.Label(root, text="Enter a request:",font=custom_font)
request_entry = tk.Entry(root,font=custom_font)
send_button = tk.Button(root, text="Send Request", command=send_request_to_server, font=custom_font)
result_label = tk.Label(root, text="",font=custom_font)

# Place widgets in the window
request_label.pack()
request_entry.pack()
send_button.pack()
result_label.pack()

# Start the Tkinter main loop
root.mainloop()