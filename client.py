import socket
import threading
outString = ''
inString = ''
alice = ''
def datalout(sock):
    global alice,outString
    while True:
        outString = input()
        outString = alice+':'+outString
        sock.send(outString)
def dataIn(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)
            if not inString:
                break
            if outString != inString:
                print(inString)
        except:
            break
alice = input("Please enter your user name:")
ip = input("Please enter you ip address:")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((ip,8888))
sock.send(alice)
thin = threading.Thread(target=dataIn(),args=(sock,))
thin.start()
thout = threading.Thread(target=datalout(),args=(sock,))
thout.start()