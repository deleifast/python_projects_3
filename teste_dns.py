import socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
dns_google = socket.gethostbyname('dns.google')

with open("ip_cx.txt", "w") as f:
	print(s.getsockname()[0], file=f)

with open('ip_cx.txt') as f, open('nslookup_cx.txt', 'w') as out:
    for line in map(str.rstrip, f):
        if line:  # skips empty lines
            try:
                subprocess.check_call(["nslookup", line],
                                         stdout=out)
            except subprocess.CalledProcessError:
                pass
	
