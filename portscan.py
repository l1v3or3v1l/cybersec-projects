import socket
import sys

TCP_IP = sys.argv[1]
TCP_PORT_RANGE = sys.argv[2]
start_port = int(TCP_PORT_RANGE.split('-')[0])
end_port = int(TCP_PORT_RANGE.split('-')[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
no_of_open_ports = 0

if (end_port >= 65536):
	print("port range 1-65535")
	sys.exit(0)

for TCP_PORT in range(start_port, end_port):
	try:
		s.connect((TCP_IP, TCP_PORT))
		s.close()
		print(f"port {TCP_PORT} open")
		no_of_open_ports += 1
	except ConnectionRefusedError:
		continue

print(f"{no_of_open_ports} ports open in {TCP_IP}")
