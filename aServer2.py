# -*- coding: utf-8 -*-
import threading
import socket
import sys
import time


class TelnetServer(threading.Thread):
 def __init__(self):
     threading.Thread.__init__(self)
     self.socketserver = socket.socket()
     self.socketserver.bind(('', 50001))
     self.socketserver.listen(5)
 def run(self):
     print('Servidor en marcha')
     while True:
         socketclient, addr = self.socketserver.accept()
         client = TelnetClient(socketclient, addr)
         client.start()
 def close(self):
     print('Servidor detenido')




class TelnetClient(threading.Thread):

 def __init__(self, socketclient, addr):
     threading.Thread.__init__(self)
     self.socketclient = socketclient
     self.addr = addr
 def run(self):
     print('Conexión: %s:%s' % (self.addr[0], self.addr[1]))
     while True:
         try:
             command, args = self.prompt()
         except socket.error:
             self.close()
             break
         if command == None:
             pass
         elif command == 'quit':
             self.close()
             break
         else:
             self.send('Comando desconocido\n')

 def send(self, msg):
     self.socketclient.send(msg.encode('utf8'))

 def recv(self):
     return self.socketclient.recv(1024).decode('utf8')[:-2]
     
 def prompt(self):
     try:
         self.send('356612022632899')
         recv_list = self.recv().split()
         print recv_list
         return recv_list[0].lower(), recv_list[1:]
     except IndexError:
         return None, []
 def close(self):
     self.socketclient.close()
     print('Desconexión: %s:%s' % (self.addr[0], self.addr[1]))


if __name__ == '__main__':
 try:
     telnetserver = TelnetServer()
     telnetserver.daemon = True
     telnetserver.start()
     while True:
         time.sleep(100)
 except KeyboardInterrupt:
     telnetserver.close()
     sys.exit()
