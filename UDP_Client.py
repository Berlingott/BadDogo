import socket

def UDP_Client(target_host, target_port):
    # create socket
    # AF_INET - socket family where HOST is an IPv4 or adress in string and PORT is an integer
    # SOCK_STREAM -  this is a UDP Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #send some data
    client.sendto(b"AAABBBCCC",(target_host,target_port))

    #receive information
    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()