import socket
import threading

object=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
object.connect(('127.0.0.1', 52460))
def textRecv(object,msg):
    while True:
        serRecv = object.recv(1025)
        print(serRecv)


while True:
    msg=input('Send Message: ')
    object.send(msg.encode('utf-8'))
    threading._start_new_thread(textRecv,(object,msg))
    if msg=='**0**':
        exit
