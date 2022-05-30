#!/usr/bin/env python3
import socket
import sys

def help():
	print(f"{sys.argv[0]} <ip> <port>")
	sys.exit(0)

def argcheck():
	if len(sys.argv) == 1 or sys.argv[1] == '-h':
		help()
	if '-' in sys.argv[2]:
		return "range"
	else:
		return "port"

def scan(TCP_IP, TCP_PORT):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((TCP_IP, TCP_PORT))
		s.close()
		print(f"port {TCP_PORT} open")
		return 1
	except ConnectionRefusedError:
		return 0

def main():
	ip = sys.argv[1]
	
	if argcheck() == "range":
		port_range = sys.argv[2]
		no_of_open_ports = 0
		start_port = int(port_range.split('-')[0])
		end_port = int(port_range.split('-')[1])
		if (end_port >= 65536 or start_port >= end_port):
			print("port range 1-65535")
			sys.exit(0)
		for port in range(start_port, end_port):
			if scan(ip, port) == 1:
				no_of_open_ports += 1	
		print(f"{no_of_open_ports} ports open in {ip}")
		
	if argcheck() == "port":
		port = int(sys.argv[2])
		if (port >= 65536):
			print("port 1-65535")
			sys.exit(0)
		if scan(ip, port) == 0:
			print(f"port {port} closed")

if __name__ == '__main__':
	main()
