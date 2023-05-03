import socket
import threading


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


def TCP_Server(IP, PORT):
    # create socket, ipv4, protocol TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binds a unique local name to the socket with descriptor socket. After calling socket(),
    #   a descriptor does not have a name associated with it. However, it does belong to a particular address family as
    #   specified when socket() is called. The exact format of a name depends on the address family.
    server.bind((IP, PORT))
    # start listenning for connection request
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        #
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
