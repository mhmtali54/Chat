import socket
import cPickle
import datetime



host = "31.170.167.146"
port = 21

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

print "asdf"
print "baglanti kuruldu"
server.send("mrb")
server.recv(1024)
name = raw_input("User Name: ")
server.sendall(name)
data = server.recv(1024)

if data == "#gir":
    while True:
     msg = raw_input(str.format("{}$ ", name))
     server.sendall(msg)
     mesajlar = cPickle.loads(server.recv(2014))
     for i in mesajlar:
         print str.format("{0}: {1}", i['name'], i['message'])
