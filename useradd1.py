import loginutility as lu
import socket
import pickle
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = ''
port = 10000
s.bind((address, port))
s.listen(5)

users = lu.UserList("accounts")
while True:
        c, clientaddress = s.accept()
        c.send("You're Connected")
        d = c.recv(1024)
        if d == "add":
                userdata = c.recv(1024)
                username, password = pickle.loads(userdata)
                users.adduser(username, password)
                print "User {} added with password of {}.".format(username, password)
                c.send("Success")
        elif d == "check":
                username, password = pickle.loads(c.recv(1024))
                if users.checkuser(username) == False:
                        c.sendall(False)
                else:
                        c.sendall(True)
        elif d == "userdump":
                c.send(pickle.dumps(users.dumpuser())

        c.close()
