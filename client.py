
import socket
import cPickle
import datetime
import colorsys

colorsys.hsv_to_rgb(200, 000, 000)
(200, 200, 200)


host = "127.0.0.1"
port = 21

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))



print"    ____ _               _            _   _            _    _     "        
print"   / ___| |__   ___  ___| | ___   _  | | | | __ _  ___| | _(_)_ __   __ _ "
print"  | |   | '_ \ / _ \/ _ \ |/ / | | | | |_| |/ _` |/ __| |/ / | '_ \ / _` |"
print"  | |___| | | |  __/  __/   <| |_| | |  _  | (_| | (__|   <| | | | | (_| |"
print"   \____|_| |_|\___|\___|_|\_\___, | |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |"
print"                              |___/                                 |___/ "

print" ____  _            _         _   _       _   "
print"| __ )| | __ _  ___| | __    | | | | __ _| |_ "
print"|  _ \| |/ _` |/ __| |/ /____| |_| |/ _` | __|"
print"| |_) | | (_| | (__|   <_____|  _  | (_| | |_ "
print"|____/|_|\__,_|\___|_|\_\    |_| |_|\__,_|\__|"
                                              

print"  ____ _           _         ____                                      "
print" / ___| |__   __ _| |__     |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  "
print"| |   | '_ \ / _` | ___|____| |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \ "
print"| |___| | | | (_| | |  |____|  __/| | | (_) | (_| | | | (_| | | | | | |"
print" \____|_| |_|\__,_| |__|    |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|"
print"                                             |___/                     "

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
        mesajlar = cPickle.loads(server.recv(1024))
        print "======================================"
        for i in mesajlar:
            print str.format("{0}: {1}", i['client'][1], i['message'])
        print "======================================"
