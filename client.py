import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.19.0.5', 45000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    message = "TIME dan diakhiri dengan karakter 13 dan karakter 10"
    
    while message.lower().strip() != 'bye':
        sock.send(message.encode())  # send message
        data = sock.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input

        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()
