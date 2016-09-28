def createCluster(name):
        connect(os.environ['WLSADMIN_ADMIN_LOGIN'], os.environ['WLSADMIN_ADMIN_PASSWORD'], 't3://wlsadmin:7001')
        try:
                edit()
                startEdit()
                cd('/')
                cmo.createCluster(name)
                cd('/Clusters/' + name)
                cmo.setClusterMessagingMode('unicast')
                cmo.setMigrationBasis('database')
                save()
                activate()
        except Exception, e:
                undo('true', 'y')

        disconnect('true')

#=========MAIN PROGRAM =========================
#name=raw_input('Please enter Cluster name:')

name = 'auto-cluster'

createCluster(name)