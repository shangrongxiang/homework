import pexpect
import sys
import os
def putPublicKey(publicKey,user,servers,port):
    for server in servers:
        child = pexpect.spawn("/usr/bin/ssh-copy-id -p %s -i %s %s@%s" %(port,publicKey,user,server))
        index = child.expect(["yes/no","password","exist",pexpect.exceptions.EOF, pexpect.TIMEOUT])
        if index != 0 and index != 1:
            child.close(force=True)
        else:
            child.sendline("yes")
            child.expect("password")
            child.sendline("12345")
            child.expect("added")
if __name__ == '__main__':
    user = "root"
    servers = ["bob"]
    port = "2222"
    publicKey = "/home/ansible/.ssh/id_rsa.pub"
    putPublicKey(publicKey,user,servers,port)