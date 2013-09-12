#!/usr/bin/env python3
#encoding=utf-8

import os
import sys
import subprocess

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
            subprocess.call("xfdesktop --reload", shell=True)
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


cls=WallpaperChange()
cls.startChange()
