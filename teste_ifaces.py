import socket

def getips(hostname):
    try:
        result = socket.getaddrinfo(hostname, None, socket.AF_INET,\
            socket.SOCK_DGRAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
        list = [x[4][0] for x in result]
        return list
    except Exception:
        print ("error")
    return ""


ips = getips('ngo-dc-01.nagumo.local')


print (''.join(ips))