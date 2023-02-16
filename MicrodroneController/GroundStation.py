#input stuff

import socket, keyboard as kb
import time

data = [0,0,0,0,0]

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while True:

    if kb.is_pressed('w'):
        data[0]=2
    elif kb.is_pressed('s'):
        data[0]=0
    else:
        data[0]=1

    if kb.is_pressed('up'):
        data[1]=2
    elif kb.is_pressed('down'):
        data[1]=0
    else:
        data[1]=1

    if kb.is_pressed('right'):
        data[2]=2
    elif kb.is_pressed('left'):
        data[2]=0
    else:
        data[2]=1

    if kb.is_pressed('e'):
        data[3]=2
    elif kb.is_pressed('q'):
        data[3]=0
    else:
        data[3]=1

    if kb.is_pressed('p'):
        data[4]=2
    elif kb.is_pressed('i'):
        data[4]=1
    elif kb.is_pressed('d'):
        data[4]=0
   
   
    packet = bytes(data)  
    UDPServerSocket.sendto(packet, ("192.168.4.1",50000))
    print(packet)
    time.sleep(0.2)