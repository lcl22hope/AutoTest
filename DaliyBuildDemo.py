#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'lcl'

import os
import sys
import git
import commands

from Logger import log
from git import Repo
from config import ServerConfiguration


reload(__import__('sys')).setdefaultencoding('utf-8')

class AutoBuild_Release:

    def __init__(self):
        os.chdir(ServerConfiguration.projectPath)
        #初始化目录
        if not os.path.exists(ServerConfiguration.src_dir):
            os.system('mkdir %s'%ServerConfiguration.src_dir)
        if not os.path.exists(ServerConfiguration.test_dir):
            os.system('mkdir %s'%ServerConfiguration.test_dir)
        if not os.path.exists(ServerConfiguration.build_dir):
            os.system('mkdir %s'%ServerConfiguration.build_dir)
        if not os.path.exists(ServerConfiguration.debug_dir):
            os.system('mkdir %s'%ServerConfiguration.debug_dir)
        if not os.path.exists(ServerConfiguration.release_dir):
            os.system('mkdir %s'%ServerConfiguration.release_dir)


        #stepID
        self.stepid = {'0':'GIT_CLONE_0',
                       '1':'BUILD_DEBUG_1',
                       '2':'RUN_TEST_2',
                       '3':'UPLOAD_TO_FTP_3',
                       '4':'EMAIL_4'}

        #step result, 0 represents Success, !0 represents Failure
        self.stepResult={'GIT'          :0,
                         'BUILD_DEBUG'  :0,
                         'RUN_TEST'     :0,
                         'UPLOAD_TO_FTP':0,
                         'EMAIL'        :0}

        #stepErr
        self.errcode = {'GIT'          :ServerConfiguration.gitError,
                        'BUILD_DEBUG'  :ServerConfiguration.buildErr,
                        'RUN_TEST'     :ServerConfiguration.testErr ,
                        'UPLOAD_TO_FTP':ServerConfiguration.ftpErr  ,
                        'EMAIL'        :ServerConfiguration.emailErr}

        #stepLog
        self.stepMsg = {'GIT'          :'',
                        'BUILD_DEBUG'  :'',
                        'RUN_TEST'     :'',
                        'UPLOAD_TO_FTP':'',
                        'EMAIL'        :''}



    def gitCheckout(self):
        print "gitCheckout step start"
        os.chdir(ServerConfiguration.src_dir)

        if os.path.exists(ServerConfiguration.git_project_dir):
            os.system('rm -frd *')

        cmd = "git clone " + ServerConfiguration.git_src_url
        out = commands.getoutput(cmd)
        # self.stepResult['GIT'] += re
        self.stepMsg['GIT']    += out
        log.i(self.stepMsg['GIT'])
        return self.stepResult['GIT']
        # myGit = git.Git()
        # myGit.clone(ServerConfiguration.git_src_url)

    def build_debug(self):
        print "build step start"
        # 利用xcodebuild、xcrun工具编译、构建、打包、安装

    def runTest(self):
        print "test cases start"
        #跑测试用例

    def uplaodToFTP(self):
        print "upload start"

    def email(self):
        print "email start"




if __name__ == '__main__':
    dailyBuild = AutoBuild_Release()
    dailyBuild.gitCheckout()
    # dailyBuild.build_debug()
    # dailyBuild.runTest()
    # dailyBuild.uplaodToFTP()
    # dailyBuild.email()
