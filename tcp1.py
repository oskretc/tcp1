#tcp1.py
from socket import *

HOST = ''
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096

try:
    print "trying to establish the server"
    serv=socket (AF_INET,SOCK_STREAM)
    serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv.bind((ADDR))
    
    print "listening"
    serv.listen(1)

    conn, addr = serv.accept() #accept the connection
    print '...connected!', addr
    conn.send('TEST')
    
except KeyboardInterrupt:
    print "closing with keyboard"
    #conn.shutdown()
    #conn.close()
    
finally:
    print "closing"
    serv.shutdown(SHUT_RDWR)
    serv.close()
        
    