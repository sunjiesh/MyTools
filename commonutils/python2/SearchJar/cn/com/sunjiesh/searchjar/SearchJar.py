#!/usr/bin/python

from os import path
import os,sys
from zipfile import ZipFile

def searchJarByClassName(dir,clsName):
    """
    读取指定className的jar文件，主要的逻辑是1、遍历目录，如果为文件，判断是否是jar文件，如果是则进一步判断是否含有class文件，如果是目录，则再次调用方法
    """
    print "begin search dir "+dir
    searchFileResult=[]
    tempFiles=os.listdir(dir)
    for tempFile in tempFiles:
        print tempFile
        if path.isfile(path.join(dir, tempFile)):
            if(tempFile.lower().endswith("jar")):
                print "read jar file "+tempFile
                clsName=clsName.replace(".", "/")
                clsName=clsName+".class"
                clsName=clsName.lower()
                print "clsName="+clsName
                for classFile in ZipFile(path.join(dir, tempFile)).namelist():
                    #print "classFile.lower()="+classFile.lower()
                    if classFile.lower()==clsName:
                        searchFileResult.append(dir+"/"+tempFile)
        elif path.isdir(path.join(dir, tempFile)):
            print "tempFile is dir"
            searchFileResult=searchFileResult+searchJarByClassName(dir+"/"+tempFile, clsName)
        else:
            pass
    #print "end search"
    return searchFileResult

if __name__ == "__main__":
    #read the sysargv
    sysArgvs=sys.argv
    sysArgvDic={};
    #遍历参数，根据前面参数开头判断参数
    for tempArgv in sysArgvs:
        print "sysArgv ="+tempArgv
        #需要查询的目录
        if tempArgv.startswith("-d"):
            dir=tempArgv[2:]
            print "dir="+dir
            if dir=="":
                print "-d参数后为空，请输入"
            else:
                sysArgvDic["dir"]=dir
        elif tempArgv.startswith("-c"):
            cls=tempArgv[2:]
            print "class="+cls
            if cls=="":
                print "-c参数后为空，请输入"
            else:
                sysArgvDic["class"]=cls
        else:
                print "其它"
    #读取dict，根据字典值调用对应的方法
    if "dir" in sysArgvDic.keys() and "class" in sysArgvDic.keys():
        print "execute def searchJarByClassName"
        searchFileResult=searchJarByClassName(sysArgvDic["dir"],sysArgvDic["class"])
        print "包含类名"+str(sysArgvDic["class"])+"的jar包有"
        for searchFile in searchFileResult:
            print searchFile


