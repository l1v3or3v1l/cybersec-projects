#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
		print("Usage: vrfy.py <ip> <usernames>")
		print("Ex: vrfy.py 192.168.56.1 users.txt")
		sys.exit(0)

with open(sys.argv[2], 'r') as file:
    data = file.read().splitlines()

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect((sys.argv[1],25))

# Receive the banner
banner = s.recv(1024)

print(banner)

for name in data:
	# VRFY a user
	s.send(str.encode('VRFY ' + name + '\r\n'))

	result = s.recv(1024)

	print(name, "\n", result, "\n")

# Close the socket
s.close()