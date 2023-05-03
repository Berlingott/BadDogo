from TCP_Client import TCP_Client
from UDP_Client import UDP_Client
from TCP_Server import TCP_Server
import socket

if __name__ == '__main__':
    #TCP_Client("www.google.com", 80)
    #UDP_Client("127.0.0.1", 1337)
    TCP_Server("0.0.0.0",9998)