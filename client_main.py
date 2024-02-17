import board
from client_request import ClientRequest
from server_response import ServerResponse

import socket
import pickle

client_socket = socket.socket()
host = socket.gethostname()
port = 42069

client_socket.connect((host, port))

while True:
    
    #   get some request
    raw_client_request = ClientRequest("stop server")
    
    processed_client_request = pickle.dumps(raw_client_request)

    client_socket.send(processed_client_request)

    raw_server_response = client_socket.recv(1024)
    processed_server_response = pickle.loads(raw_server_response)

    #   do something with the response
    print(f"Server response: '{processed_server_response.message}'")

    #   this is for one time use
    break

client_socket.close()








