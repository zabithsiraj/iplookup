#! usr/bin/env python

#This tool has been created by Zabith Siraj.
#telegram: @zabithsiraj
#This is a simple reverse ip lookop
import os
os.system("clear")
banner='''
.____                  __                 
|    |    ___________ |  | _____________  
|    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
|    |__(  <_> |  <_> )    <|  |  /  |_> >
|_______ \____/ \____/|__|_ \____/|   __/ 
        \/                 \/     |__|    
         #Created by zabith siraj
        '''
        
print(banner)
cmd= "curl -s https://api.hackertarget.com/reverseiplookup/?q=" + input("[-]Enter Site Name : ")
print("[-]searching for credentials")
print("[-]Please Wait .... \033[1;33;40m")
os.system(cmd)
exit(1)
