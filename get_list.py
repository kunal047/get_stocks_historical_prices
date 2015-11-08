import xlrd
from urllib import request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import socks
import socket
socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket
print(requests.get("http://icanhazip.com").text) #your dummy ip address
file = "~/Github/Active.xlsx" #address where Active.xlsx file is stored.
work = xlrd.open_workbook(file)
sheet = work.sheet_by_index(0)
for i in range(1, -):  #enter the range of cell to get the index of the stock
    val = sheet.cell_value(i, 1)
    url = "https://in.finance.yahoo.com/q/hp?s=" + val + '.BO' #.BO extension is for BSE stock index of india
    #soup = BeautifulSoup(url)
    response = requests.get(url)
    data = response.text
    sou = BeautifulSoup(data, parseOnlyThese=SoupStrainer("p"))
    x = sou.findAll("a")
    for tr in x:
        links = tr.get('href')
        #print(links)
        break
    response = request.urlopen(links)
    csv = response.read()
    # Save the string to a file
    csvstr = str(csv).strip("b'")
    lines = csvstr.split("\\n")
    f = open(val + ".csv", "w")
    for line in lines:
        f.write(line + "\n")
    f.close()
