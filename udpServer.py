'''
Created on Nov 24, 2018

@author: bpr
'''
import socket


 
localIP     = "0"
localPort   = 50001
bufferSize  = 1024


msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

def serverInitialize():
    from listener import runProcess

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    
    print("UDP server up and listening")
    
    # Listen for incoming datagrams
    while(True):
    
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
    
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)

    
        if(message == "MEASURE"):
            
            proc_result = runProcess()
        
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode(proc_result), address)
    
    
    