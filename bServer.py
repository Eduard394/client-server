# -*- coding: utf-8 -*-
import socket, string
#import MySQLdb



HOST = ""
PORT = 50001

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
    print u"Listen to " + str(PORT)
    srv.listen(1)             
    sock, addr = srv.accept()
    while 1:
        pal = sock.recv(2048)
        if not pal: 
            break
        print u"Recieved %s:%s:" % addr, pal
       # lap = write_message(pal)
    sock.close()