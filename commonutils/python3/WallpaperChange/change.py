#!/usr/bin/env python3
#encoding=utf-8

import os
import sys
import subprocess
import random

class WallpaperChange:
    """
    桌面壁纸转换
    """
    
    def __init__(self):
        """初始化"""
        print("开始执行程序")
        
    def startChange(self):
        """根据不同环境，调用系统命令，更换壁纸"""
        print("开始更换壁纸")
        #判断桌面环境
        platformName=self.getPlatform()
        print("当前的桌面环境是"+platformName)
        if platformName=="XFCE":
            #subprocess.call("xfdesktop --reload", shell=True)
            print("change wallpaper")
            wallpaparList=self.getWallpaperList()
            print(wallpaparList)
            randomWallpapaper=wallpaparList[random.randrange(0,len(wallpaparList))]
            status, output = subprocess.getstatusoutput("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s %s" %randomWallpapaper)
        print("结束更换壁纸")
    
    def getPlatform(self):
        #判断MacOS
        if sys.platform in ('mac', 'darwin'):
            return "Mac"
        #判断桌面环境
        if not self.get_output("plasma-desktop"):
            return "KDE"
        if not self.get_output("gnome-panel") and os.environ.get("DESKTOP_SESSION") == "gnome":
            return "Gnome"
        if not self.get_output("xfce4-panel"):
            return "XFCE"
        if not self.get_output("mate-panel"):
            return "MATE"
        if not self.get_output("lxpanel"):
            return "LXDE"

        return "GnomeShell"
     
    def get_output(self, cmd):
        status, output = subprocess.getstatusoutput("ps -A | grep %s" %cmd)
        return status
    
    def getWallpaperList(self):
            
        wallpaparList=[]
        
        paramDict={}
        
        #read config file
        configFile=open("config.cfg",mode="r",encoding="utf-8")
        for line in configFile:
            line=line[:]
            param=line.split("=")
            paramName=param[0]
            paramValue=param[1]
            paramDict[paramName]=paramValue
        configFile.close()
        
        #read wallpaperdir
        dir=paramDict["wallpaper.dir"]
        dir=dir.replace("\n","")
        print(dir)
        wallpaparList=self.getWallpaperFileList(dir,wallpaparList) 
        return wallpaparList
        
    
    def getWallpaperFileList(self, dir,wallpaparList):
        """read dir and get wallpaper file"""
        print("list dir imagefile---"+dir)
        if os.path.exists(dir):
            print("文件夹存在")
            for imageFile in os.listdir(dir):
                if os.path.isfile(dir+"/"+imageFile) :
                    if imageFile.lower().endswith(".jpg"):
                        wallpaparList.append(dir+"/"+imageFile)
                    else:
                        print (imageFile+"is not jpg file")
                else:
                    wallpaparList=wallpaparList+getWallpaperFileList(dir+"/"+imageFile,wallpaparList)
        else:
            print("文件夹"+dir+"不存在")
        return wallpaparList
        
cls=WallpaperChange()
cls.startChange()
