# from alive_progress import alive_bar
from optparse import OptionParser 

import socket,subprocess
from pathlib import PurePath
import sys,os
subprocess.call('',shell=True)

# getting the needed arguments to run the program
parser = OptionParser()
parser.add_option("-f", dest="file_name",
                  help="file path ")

parser.add_option("-i", dest="ip_address", help="connect to remote host (ex:localhost)")
parser.add_option("-p", dest="port",
                  help="port")
option,args = parser.parse_args()
ip=option.ip_address
port=option.port
file_name=option.file_name
if not ip or not port or not file_name:
     print(''' 
Usage: send_files.py [options]
   Options:
  -h, --help      show this help message and exit
  -f FILE         file path
  -i IP_ADDRESS   connect to remote host (ex:localhost)
  -p PORT         port
  -E ENCRYPTION   this feature coming soon''')
    
    
    exit()
if os.path.isdir(file_name):
    print('err')
# initializing the buffer size

buff = 1024

# connecting to the server machine

s = socket.socket()
s.connect((ip, port))
print("Connected to {}:{}".format(ip, port))

file = open(file_name, "rb")

# sending name of the file to server
# and waiting for a reply as an acknowledgement that 
# file name is recieved
file_name=PurePath(file_name).name
print(file_name)
s.send(file_name.encode())    
ack = s.recv(buff)

# if we recieve an acknowledgement then we can start
# running a progress bar and transer the file

if ack.decode() == file_name:
    
    #file_size = Path(file_name).stat().st_size
    
    # with alive_bar(file_size) as bar:
        
        # reding data of file and sending it as messages
        # until we send the last bit of the file

    msg = file.read(buff)
    while msg:
        s.send(msg)
        msg = file.read(buff)
            
            # moving the bar 
            
            # for i in range(buff): bar()
                
# cleaning everything up after file has been transfered
    
print("Sent file {} successfully".format(file_name))
file.close()
s.close()
