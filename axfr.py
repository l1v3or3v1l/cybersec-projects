from sys import argv
import socket
import dns.resolver
import dns.zone
import dns.query
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *

domain = argv[1]
data = set()
name_servers = ""

try:
	name_servers = dns.resolver.resolve(domain, "NS")
except dns.resolver.NoAnswer:
	print("DNS resolving error, recheck domain name")

for ns_host in name_servers:
	ns = socket.gethostbyname(str(ns_host))
	try:
	    zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
	except DNSException:
	    continue

	for (name, ttl, rdata) in zone.iterate_rdatas('A'):
	    data.add(f"{name}.{domain} {rdata}")

for x in sorted(data):
	print(x)