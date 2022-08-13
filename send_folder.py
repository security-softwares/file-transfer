
import os,subprocess
subprocess.call('',shell=True)
pwd=os.getcwd
from optparse import OptionParser 
# parser = OptionParser()

# group = OptionGroup(parser, "Dangerous Options",
#                     "Caution: use these options at your own risk.  "
#                     "It is believed that some of them bite.")
# group.add_option("-g", action="store_true", help="Group option.")
# parser.add_option_group(group)
# options, args = group.parser.parse_args()
parser = OptionParser()
parser.add_option("-f", dest="folder_name",
                  help="folder path ")

parser.add_option("-i", dest="ip_address", help="connect to remote host (ex:localhost)")
parser.add_option("-p", dest="port",
                  help="port")
parser.add_option("-E", dest="encryption",
                  help="this feature coming soon")
option,args = parser.parse_args()

folder=option.folder_name
ip=option.ip_address
port=option.port
encr=option.encryption
if  not ip or not port or not folder:
    print(''' 
Usage: send.py [options]

Options:
  -h, --help      show this help message and exit
  -f FOLDER_NAME  folder path
  -i IP_ADDRESS   connect to remote host (ex:localhost)
  -p PORT         port
  -E ENCRYPTION   this feature coming soon''')
                                                
        
        
    
    exit()                                   
folder=folder.strip()

ln=len(str(folder))
f=folder[ln-1]                                     
if f in  '/' or  f in "\\":
    folder=folder[:-1]
fp=''
p=os.name            
if p=='nt':
    fp=folder+'\\'
else:
   fp=folder+'/' 
fl=[]
file=[] 

if os.path.isdir(folder):
    print('sending files of the folder ',folder)
    fd=os.listdir(folder)

    for i in range(len(fd)):
        if os.path.isfile(fp+fd[i]):
            file.append(fp+fd[i])
           
        if os.path.isdir(fp+fd[i]):
            fl.append(fp+fd[i])
            

else:
        print('error occured its not folder \n    or ')
dl=[]
for j in file:
    if j not in dl:
        dl.append(j)

fdr=[]
for k in fl:
    if k not in fdr:
        fdr.append(k)

# print(fl)
# print(file)
for kis in dl:
    if p=='nt':
        
        os.system(f'python send_files.py -f "{kis}" -i {ip} -p {port}')

    else:

        os.system(f'python3 send_files.py -f "{kis}" -i {ip} -p {port} ')
for kk in fdr:
    if p=='nt':
        
        os.system(f'python send_folder.py -f "{kk}" -i {ip} -p {port}')
        print(i)
    else:

        os.system(f'python3 send_folder.py  -f "{kk}" -i {ip} -p {port} ')
