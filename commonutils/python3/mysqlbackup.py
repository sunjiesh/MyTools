#!/usr/bin/env python3
#encoding=utf-8

import subprocess

class MysqlBackup:
    def backup(self):
        try:
            paramDict={}
            
            #read config file
            configFile=open("mysqlbackup.cfg",mode="r",encoding="utf-8")
            for line in configFile:
                line=line[:-1]
                param=line.split("=")
                paramName=param[0]
                paramValue=param[1]
                paramDict[paramName]=paramValue
            configFile.close()
            
            #read dict
            mysqlHost=paramDict["mysql.host"]
            mysqlPort=paramDict["mysql.port"]
            mysqlUsername=paramDict["mysql.username"]
            mysqlPassword=paramDict["mysql.password"]
            mysqlDbname=paramDict["mysql.dbname"]
            backupDir=paramDict["backup.dir"]
            lessParam=False
            if mysqlHost=="":
               print("Please Setup the mysql.host in the mysqlbackup.cfg")
               lessParam=True
               return False
            if mysqlPort=="":
               mysqlPort="3306"
            if mysqlUsername=="":
               print("Please Setup the mysql.username in the mysqlbackup.cfg")
               lessParam=True
               return False
            if mysqlPassword=="":
               print("Please Setup the mysql.password in the mysqlbackup.cfg")
               lessParam=True
               return False
            if mysqlDbname=="":
               print("Please Setup the mysql.dbname in the mysqlbackup.cfg")
               lessParam=True
               return False
            if backupDir=="":
               backupDir="/tmp"
            if not lessParam:
               
            
               
               #generate command
               cmdParam=[]
               cmdParam.append("mysqldump")
               cmdParam.append("-h"+mysqlHost)
               cmdParam.append("-P"+mysqlPort)
               cmdParam.append("-u"+mysqlUsername)
               cmdParam.append("-p"+mysqlPassword)
               cmdParam.append(mysqlDbname+">"+backupDir+"/"+mysqlDbname+".sql")
               print("execute command is "+' '.join(cmdParam))
               
               subprocess.call(' '.join(cmdParam), shell=True)
               print("execute backup mysqldb "+mysqlDbname+" finish")
               
        except IOError as err:
            print("I/O error: {0}".format(err))

mysqlBackup=MysqlBackup()
mysqlBackup.backup()