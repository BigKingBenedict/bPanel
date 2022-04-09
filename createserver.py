import os
import urllib.request

def create(user,sv,name,ram,cpu):
    print("Creating new Server ("+str(name)+") for USER: "+str(user)+", on VERSION: "+str(sv)+", with RAM: "+str(ram)+"GB and CPU: "+str(cpu)+"%.")

    #create server.info
    os.makedirs('servers/server-'+str(user)+'-'+str(name))
    with open('servers/server-'+str(user)+'-'+str(name)+'/server.info', 'w') as f:
       f.write('user:'+str(user))
       f.write('\nsv:'+str(sv))
       f.write('\nname:'+str(name))
       f.write('\nram:'+str(ram))
       f.write('\ncpu:'+str(cpu))

    #get version download link
    with open('serverversions/'+str(sv)+'.txt') as f:
       link = f.readline()

    #download the file 
    urllib.request.urlretrieve(str(link), 'servers/server-'+str(user)+'-'+str(name)+'/server.jar')   

    #create start.sh and start.bat 
    startCode="java -Xmx"+str(ram)+"G -jar server.jar nogui"
    with open('servers/server-'+str(user)+'-'+str(name)+'/start.sh', 'w') as f:
       f.write(str(startCode))

    with open('servers/server-'+str(user)+'-'+str(name)+'/start.bat', 'w') as f:
       f.write(str(startCode))   

    #start server (ON WIN)
    exec("servers/server-"+str(user)+"-"+str(name)+"/start.bat")
