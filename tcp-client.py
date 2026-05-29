from socket import AF_INET, SOCK_STREAM
import socket


HOST = input("Enter a target host")
PORT = int(input("Enter a target port"))
DATA = input("What do you want to send to the client?")

client = socket.socket(AF_INET, SOCK_STREAM)

client.connect((HOST, PORT))
client.send(b"{}".format(DATA))

response  = client.recv(4096)
print(response.decode())
client.close()
