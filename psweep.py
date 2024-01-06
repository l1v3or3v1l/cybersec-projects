from sys import argv, exit
from subprocess import call, DEVNULL

if len(argv) == 1:
	print(f"""Usage: 
	{argv[0]} <netid> [-v]
Eg:
	{argv[0]} 192.168.1
	{argv[0]} 192.168.2 -v""")
	exit()

netid = argv[1]
if len(argv) == 3:
	verbose = argv[2]
else:
	verbose = 0

for hostid in range(1, 255):
	hostname = netid + "." + str(hostid)
	if call(["ping", "-c", "1", hostname],
		stdout=DEVNULL,
		stderr=DEVNULL) == 0:
			print(f"{hostname} is up!")
	elif verbose == "-v":
  			print(f"{hostname} is down!")