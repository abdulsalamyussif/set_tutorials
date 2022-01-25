import socket
mysocked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocked.connect(('www.py4e.org', 80))
cmd = 'GET http://www.py4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysocked.send(cmd)

while True:
    data = mysocked.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysocked.close()