from socket import AF_INET, SOCK_DGRAM
import socket

# ======+=#
# HELPERS #
# ======= #

def init_client():
    return client.socket(AF_INET, SOCK_DGRAM)

# =============== #
# INPUT VARIABLES #
# =============== #
HOST = input("Enter a target host...")
PORT = int(input("Enter a target port..."))
DATA = input("What would you like to send to the target?")


# ============ #
# SEND REQUEST #
# ============ #
client = init_client()
client.send(b"{}".format(DATA), (HOST, PORT))


# =============== #
# OUTPUT RESPONSE #
# =============== #
data, addr = client.recvfrom(4096)
print(data.decode())

# ======= #
# CLEANUP #
# ======= #
client.close()

