'''
Created on 2015-06-02 15:42:55
@author: Aaron
'''
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import shutil
import logging
from config import ServerConfiguration



class FileLogger(object):
    def __init__(self,path=ServerConfiguration.logFile):
        self.__path   = path
        self.__logger = logging.getLogger()
        hdlr = logging.FileHandler(path)
        msgFormat = logging.Formatter('%(asctime)s  %(levelname)  %(message)s')
        hdlr.setFormatter(msgFormat)
        self.__logger.addHandler(hdlr)
        self.__logger.setLevel(logging.NOTSET)

    def i(self,msg=''):
        print(msg)
        self.__logger.info(msg)

    def e(self,msg=''):
        print(msg)
        self.__logger.error(msg)

log = FileLogger(ServerConfiguration.logFile)
log.i("-----------------LOG initialized")