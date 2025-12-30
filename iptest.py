import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("local ip:", local_ip)

import urllib.request

public_ip = urllib.request.urlopen("https://api.ipify.org").read().decode().strip()
print("public ip:", public_ip)