import sys

import socket

import pygame
from pygame.locals import *
import sys

s = socket.socket()

print("Socket successfully created")

port = 27339
data = '0'

# s.connect(("192.168.97.140", port))
# print("socket binded to %s" % (port))
# s.listen(5)
# print("socket is listening")
# c, addr = s.accept()
# print('Got connection from', addr)
server = "192.168.137.46"
port = 27339
addr = (server, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)


def dataPacket(data, data1, data2, data3, data4, data5):
    sendData("m" + "s" + data + "f" + data1 +
             "n" + data2 + data3 + data4 + data5)


def sendData(me):

    while True:

        a = me.encode()
        client.sendall(a)
        return


pygame.init()
display = pygame.display.set_mode((300, 300))

while (1):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # print("Key A has been pressed")
                data = 'a'
                # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                # print("Key A has been released")
                data = '0'
                # sendData(me='ar')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # print("Key W has been pressed")
                data = 'w'
            # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                # print("Key W has been released")
                data = '0'
                # sendData(me='ar')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # print("Key S has been pressed")
                data = 's'
                # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                # print("Key S has been released")
                data = '0'
                # sendData(me='ar')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # print("Key D has been pressed")
                data = 'd'
                # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                # print("Key D has been released")
                data = '0'
                # sendData(me='ar')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # print("Key C has been pressed")
                data = 'c'
                # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                # print("Key C has been released")
                data = '0'
                # sendData(me='ar')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                # print("Key O has been pressed")
                data = 'o'
                # sendData(me='a')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o:
                # print("Key O has been released")
                data = '0'
                # sendData(me='ar')

        sendData(data)
        print(data)
