import subprocess

with open('rede.txt') as f, open('nslookup.txt', 'w') as out:
    for line in map(str.rstrip, f):
        if line:  # skips empty lines
            try:
                subprocess.check_call(["nslookup", line],
                                         stdout=out)
            except subprocess.CalledProcessError:
                pass
