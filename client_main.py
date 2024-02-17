import board

import socket
import pickle

client_socket = socket.socket()
host = socket.gethostname()
port = 42069

client_socket.connect((host, port))

while True:
    
    #   get some request
    raw_client_request = "stop server"
    
    client_request = pickle.dumps(raw_client_request)

    client_socket.send(client_request)

    raw_server_response = client_socket.recv(1024)
    server_response = pickle.loads(raw_server_response)

    #   do something with the response
    print(f"Server response: '{server_response}'")

    #   this is for one time use
    break

client_socket.close()








