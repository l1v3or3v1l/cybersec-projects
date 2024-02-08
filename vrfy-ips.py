#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
		print("Usage: vrfy.py <username> <ip-file>")
		print("Ex: vrfy.py root ips.txt")
		sys.exit(0)

with open(sys.argv[2], 'r') as file:
    data = file.read().splitlines()

for ip in data:
	# Create a Socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to the Server
	print(ip)
	connect = s.connect((ip,25))

	# Receive the banner
	banner = s.recv(1024)

	print(banner)

	# VRFY a user
	s.send(str.encode('VRFY ' + sys.argv[1] + '\r\n'))

	result = s.recv(1024)

	print(result, "\n")

	# Close the socket
	s.close()