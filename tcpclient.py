# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:40:19 2018

@author: Administrator
"""
import socket
PORT=7788
BUFFSIZE=1024
HOST='118.89.237.230'
ADDR=(HOST,PORT)
tcpclient=socket.socket()
tcpclient.connect(ADDR)
data={"src":"11111","sr":"21121"}
#while True:
    #data=input(">")
    #if not data:
       #break
tcpclient.send(str(data).encode())
    
tcpclient.close()
                   
