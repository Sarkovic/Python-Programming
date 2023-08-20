import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 8888
# Get the host ipv4 address
SERVER = '192.168.0.104'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
