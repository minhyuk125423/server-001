import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("local ip:", local_ip)