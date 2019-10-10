import socket

hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
target = '{}.{}.{}'.format(hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('168.235.64.203', 50001))

# send some data (in this case a HTTP GET request)

client.send('SKP08 $GPRMC,211553.00,A,0444.873862,N,07539.872281,W,21.8,346.9,091019,4.4,E,A*1F')
#client.send('GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld))

# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)

print response