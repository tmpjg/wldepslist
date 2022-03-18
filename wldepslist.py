connect('user','password','t3://weblogic.local:7001')
cd('AppDeployments')
deplymentsList=cmo.getAppDeployments()
domainConfig()
for app in deplymentsList:
    cd ('/AppDeployments/'+app.getName()+'/Targets')
    mytargets = ls(returnMap='true')
    for targetinst in mytargets:
        domainRuntime()
        cd('AppRuntimeStateRuntime')
        cd('AppRuntimeStateRuntime')
        curstate4 = cmo.getCurrentState(app.getName(),targetinst)
        domainConfig()
        cd('/AppDeployments/'+app.getName()+'/Targets/'+targetinst)
        myType = cmo.getType()
        if myType == 'Cluster':
            Servers = cd('/AppDeployments/'+app.getName()+'/Targets/'+targetinst+'/Servers')
            myServers = ls(returnMap='true')
            for server in myServers:
                cd('/AppDeployments/'+app.getName()+'/Targets/'+targetinst+'/Servers/'+server)
                listenaddress = str(get('ListenAddress'))
                listenport = str(get('ListenPort'))
                print "DEPLOY;"+app.getApplicationName()+";"+curstate4+";"+targetinst+";"+listenaddress+":"+listenport+";"+app.getAbsoluteSourcePath()
        elif myType == 'Server':
            cd('/AppDeployments/'+app.getName()+'/Targets/'+targetinst)
            listenaddress = str(get('ListenAddress'))
            listenport = str(get('ListenPort'))
            print "DEPLOY;"+app.getApplicationName()+";"+curstate4+";"+targetinst+";"+listenaddress+":"+listenport+";"+app.getAbsoluteSourcePath()
