import socket


def TCP_Client(target_host, target_port):
    # create socket
    # AF_INET - socket family where HOST is an IPv4 or adress in string and PORT is an integer
    # SOCK_STREAM - Socket type two-way byte streams with a
    #   transmission mechanism for stream data. This socket type transmits data
    #   on a reliable basis, in order, and with out-of-band capabilities.
    #   IN OTHER WORD: this is a TCP Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # Send data
    client.send(b"GET / http/1.1\r\nHost: google.com\r\n\r\n")

    # receive and print response
    response = client.recv(4096)

    print(response.decode())

    # clise socket/connection
    client.close()
