import subprocess

with open('dns.txt', 'r') as i, open('dns.txt', 'w') as o:
   for line in i:
     if line.split(): # skips empty lines
        proc = subprocess.Popen(["nslookup", line.split()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        stdout_data, stderr_data = proc.communicate(0)
        fqdn = stdout_data.split(b'Server:  ')[1].split(b'\r\n')[0]
        o.write('{}\n'.format(fqdn))
        print(o)