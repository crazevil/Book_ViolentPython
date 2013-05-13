import argparse
import time
from socket import *
from threading import *


screenlock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
	
    try:
    	connSkt = socket(AF_INET, SOCK_STREAM)
    	connSkt.connect(tgtHost, tgtPort)
    	connSkt.send('ViolentPython\r\n')
    	results = connSkt.recv(100)
    	screenlock.acquire()
    	print ('[+]%d/tcp open'% tgtPort)
    	print ('[+]' + str(results))
		
    except:
    	screenlock.acquire()
    	print ('[-]%d/tcp closed'% tgtPort)
		
    finally:
    	screenlock.release()
    	connSkt.close()
        
        
##########################################################
def portScan(tgtHost, tgtPorts):
	
    try:
    	tgtIP = gethostbyname(tgtHost)
		
    except:
    	print ("[-] Cannot resolve '%s': Unknown host", tgtHost)
    	return
		
    try:
    	tgtName = gethostbyaddress(tgtIP)
    	print ('\n[+] Scan Results for: %s'%tgtName)
	
    except:
    	print ('\n[+] Scan Results for: %s'%tgtIP)
		
    setdefaulttimeout(1)
	
    for tgtPort in tgtPorts:
    	t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
    	t.start()
        
		
    time.sleep(1)

##########################################################
def main():
    parser = argparse.ArgumentParser(description='Scan Some Ports.....')
    parser.add_argument('-H', dest='TargetHost',  \
                   help='specify target host')
    
    parser.add_argument('-p', dest='TargetPort', type=int, nargs='*', \
                   help='specify target port[s] separed by space')

    args = parser.parse_args()
    print (args)
    tgtHost = args.TargetHost
    tgtPorts = args.TargetPort
        
    print (tgtHost)
    print (tgtPorts)
    
    if (tgtHost == None) | (len(tgtPorts) == 0) :
        parser.print_help()
        exit(0)
    
    portScan(tgtHost, tgtPorts)
    
########################################################## 
if __name__ == "__main__":
    main()