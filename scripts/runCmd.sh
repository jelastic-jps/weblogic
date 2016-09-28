#!/bin/sh

. /u01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh;

if [ $SERVER_ROLE == "admin" ]; then

${DOMAIN_HOME}/bin/startWebLogic.sh &>> /var/log/run.log &

        if [ ! -f ${DOMAIN_HOME}/createCluster.lock ]; then
                while (true); 
                        do fuser -n tcp ${ADMIN_PORT} &&
                        {
                                wlst.sh -skipWLSModuleScanning ${DOMAIN_HOME}/createCluster.py &>> /var/log/run.log;
                                touch -f ${DOMAIN_HOME}/createCluster.lock;
                                break;
                        } || sleep 2s;
                done
        fi
fi

if [ $SERVER_ROLE == "managed" ]; then

        while (true); 
                do echo "quit" |
                telnet wlsadmin ${ADMIN_PORT} |
                grep -q "Escape character is" &&
                {
                        if [ ! -f ${DOMAIN_HOME}/createManagedServer.lock ]; then
                                wlst.sh -skipWLSModuleScanning ${DOMAIN_HOME}/createManagedServer.py &>> /var/log/run.log; 
                                touch -f ${DOMAIN_HOME}/createManagedServer.lock;
                        fi

                        fuser -n tcp ${PORT} || ${DOMAIN_HOME}/bin/startManagedWebLogic.sh ${HOSTNAME} wlsadmin:${ADMIN_PORT};
                        #break; 
                } || sleep 2s;
        done
fi

