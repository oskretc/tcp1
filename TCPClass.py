#TCPClass.py
from socket import *

class C3POServer:
    
    """
    A socket Class
    """
    sock=None
    def __init__(self, sock=None, HOST='' , PORT=29876):
        ADDR = (HOST,PORT)
        BUFSIZE = 4096
        if sock is None:
            self.sock=socket(AF_INET, SOCK_STREAM)
            self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.sock.bind((ADDR))
        else:
            self.sock=sock
    def StartListen(self):
        self.sock.listen(1)
        
    def DoConnect(self):
        conn, addr = self.sock.accept()
        self.Connection=conn
        self.Address=addr
        
    
    def SendData(self, DataOut):
        LengthBuf="%04X" % len(DataOut)
        self.Connection.send(LengthBuf + DataOut)
    def RecvData(self):
        bufsize=int(self.Connection.recv(4),16)
        DataIn=self.Connection.recv(bufsize)
        return DataIn
    
    def CloseConnection(self):
        self.Connection.close()
    def CloseServer(self):
        self.sock.shutdown(SHUT_RDWR)
        self.sock.close()