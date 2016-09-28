import os
import socket

def deleteMS(name):
        connect(os.environ['WLSADMIN_ADMIN_LOGIN'], os.environ['WLSADMIN_ADMIN_PASSWORD'], 't3://wlsadmin:7001')
        try:
                edit()
                startEdit(60000, 120000, 'true')
                shutdown(name,'Server','true',1000,force='true', block='true')
                delete(name+ ' (migratable)', 'MigratableTarget')
                delete(name,'Server')
                save()
                activate()
        except Exception, e:
                print e
                undo('true', 'y')
                cancelEdit('y')

        disconnect('true')

#=========MAIN PROGRAM =========================

name = socket.gethostname()
deleteMS(name)