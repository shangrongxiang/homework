import socket
import threading
def Node(ss):
       global data
       if conn.acquire():
            data = ss
            con.notifyAll()
            con.release()
def clientIn(conn,alice):
    global data
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
                Node(temp)
                print(data)
        except:
            Node(alice+'leavers the room!')
            print(data)
            return

def clientout(conn,alice):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return

data = ''
con = threading.Condition()
Host = input("Please enter your ip address")
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(Host,port)
s.listen(s)

while True:
    conn,addr = s.accept()
    print('connected with'+addr[0]+':'+str(addr[1]))
    alice = conn.recv(1024)
    Node("welcome")
    print(data)
    conn.send(data)
    threading.Thread(target=,args=(conn,alice)).start()
    threading.Thread(target=, args=(conn, alice)).start()