#!/usr/bin/python
# -*- coding:utf-8 -*-


class ServerConfiguration(object):
    '''
    —project
      —src
      —test
      —build
      —debug
      —release
    '''
    #directory setting
    projectPath   = '/Users/lcl/Downloads/AutoTestDemo/'
    src_dir       = projectPath + 'src'
    test_dir      = projectPath + 'test'
    build_dir     = projectPath + 'build'
    debug_dir     = projectPath + 'debug'
    release_dir   = projectPath + 'release'

    #src_project
    git_project_dir = src_dir + '/YiDa'
    git_src_url     = 'https://github.com/lcl22hope/YiDa.git'
    git_user        = 'lcl22hope'
    git_ass         = 'lushu_5857'

    ftpUser       = 'admin'
    ftpPass       = 'admin'

    certiPath     = ''
    profilePath   = ''


    gitError      = '501'
    buildErr      = '502'
    testErr       = '503'
    ftpErr        = '504'
    emailErr      = '505'

    logFile       = '/tmp/log.txt'