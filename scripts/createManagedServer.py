import os
import socket

def createMS(name, port, cluster):
        connect(os.environ['WLSADMIN_ADMIN_LOGIN'], os.environ['WLSADMIN_ADMIN_PASSWORD'], 't3://wlsadmin:7001')
        try:
                edit()
                startEdit(60000, 120000, 'true')
                cd('/')
                cmo.createServer(name)
                cd('/Servers/' + name)
                cmo.setListenPort(port)
                cmo.setListenAddress(name)
                cmo.setCluster(getMBean('/Clusters/' + cluster))
                save()
                activate()
        except Exception, e:
                print e
                undo('true', 'y')
                cancelEdit('y')

        disconnect('true')

#=========MAIN PROGRAM =========================

name = socket.gethostname()
port = int(os.environ['PORT'])

cluster = 'auto-cluster'

createMS(name, port, cluster)