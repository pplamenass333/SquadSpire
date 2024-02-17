import board
from client_request import ClientRequest
from server_response import ServerResponse

import socket
import threading
import pickle

def handle_client(client_socket, addr):
    while True:
        raw_client_request = client_socket.recv(1024)

        #   if the client doesn't send a request
        if not raw_client_request:
            break

        processed_client_request = pickle.loads(raw_client_request)

        #   do something with the request
        if processed_client_request.message == "stop server":
            server_is_on = False
        client_request_message = processed_client_request.message
        processed_server_response = ServerResponse(f"Server received: {client_request_message}")
        print(processed_server_response.message)

        raw_server_response = pickle.dumps(processed_server_response)

        client_socket.send(raw_server_response)

    client_socket.close()


#   main code

server_socket = socket.socket()
host = socket.gethostname()
port = 42069
server_is_on = True #   in the future add a stop thread that stops the server

server_socket.bind((host, port))
server_socket.listen()

print("The server is on!")

while True:
    client_socket, addr = server_socket.accept()

    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()








