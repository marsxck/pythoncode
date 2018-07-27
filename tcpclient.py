# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:40:19 2018

@author: Administrator
"""
import socket
PORT=1234
BUFFSIZE=1024
HOST='10.3.9.152'
ADDR=(HOST,PORT)
tcpclient=socket.socket()
tcpclient.connect(ADDR)
i=0

while True:
    i=i+1
    data=input(">");
    tcpclient.send(str(data).encode())
    if not data:
       break   
    print(tcpclient.recv(2024))
    
tcpclient.close()
                   
