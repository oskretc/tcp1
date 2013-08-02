#tcp1.py
#from socket import *
from TCPClass import C3POServer
HOST = ''
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096






    
print "trying to establish the server"    
s=C3POServer()


slow=1
    
try:
    while 1:
        
        if slow:
            print "listening slow"
            s.StartListen()
            s.DoConnect()
            print '...connected!', s.Address

            DataIn=s.RecvData()   #Receive Commands
            s.SendData(DataIn + "OK")     #Send ACK on the Command

            s.CloseConnection()
            
        else:
            print "listening fast"
            s.StartListen()
            s.DoConnect() #accept the connection
            DataIn=""
            while DataIn != "CloseConnection":
                try:
                    DataIn=s.RecvData()   #Receive Commands
                    s.SendData(DataIn)     #Send ACK on the Command
                except ValueError:
                    print "error"
            s.CloseConnection()
    
except KeyboardInterrupt:
    print "closing with keyboard"
    #conn.shutdown()
    #conn.close()
    
finally:
    print "closing"
    s.CloseServer
        
    