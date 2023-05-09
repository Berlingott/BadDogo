import argparse
import textwrap
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
from TCP_Client import TCP_Client
from UDP_Client import UDP_Client
from TCP_Server import TCP_Server
import socket
from netcat import execute
if __name__ == '__main__':
    #TCP_Client("www.google.com", 80)
    #UDP_Client("127.0.0.1", 1337)
    #TCP_Server("0.0.0.0",9998)
    parser = argparse.PARSER(
        description='BHP NET TOOL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell 
        netcat.py -t 192.168.1.108 -p 5555 -l -u=test.txt # uploadfiles 
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        '''))


    )