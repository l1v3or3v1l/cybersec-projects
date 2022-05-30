#!/usr/bin/env python3
import requests

num = 1
id = input('use Dev tools to find, eg [ced1adbb79950e2f77944a3b23be978df94f22d6] \n Enter id from wistia embed url : ')
filename = input('filename : ')

while True:
	url = f"https://embedwistia-a.akamaihd.net/deliveries/{id}.m3u8/v2/seg-{num}-v1-a1.ts"
	print(url)
	resp = requests.get(url, allow_redirects=True)
	open(filename, 'ab').write(resp.content)
	if resp.status_code == 404:
		break
	num+=1
