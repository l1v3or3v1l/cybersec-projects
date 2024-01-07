from sys import argv, exit
import re

if len(argv) < 3:
	print(f"""Usage: 
	{argv[0]} <filetosearch> <extension>
Eg:
	{argv[0]} access_log.txt js""")
	exit()

lines = open(argv[1], 'r').read()

result = re.findall(r'[a-z0-9.]+\.js', lines)

result = list(sorted(set(result)))

for x in result:
	print(x)