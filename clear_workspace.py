'''
Created on 9 Aug 2019

@author: sivasp
'''

import os, fnmatch, subprocess

def clearWorkspaces():
    print('Clear workspaces - invokes "make cleanclean" on every build folder in /export/../psivashanmugam/')
    script_path = os.getcwd()

    for root, dirs, files in os.walk("./../../temp/"):
        for name in files:
            if fnmatch.fnmatch(name, 'Makefile.ocz'):
                print(root)
                os.chdir(root)
                subprocess.call("make cleanclean", shell=True)
                os.chdir(script_path)
    print('-----------------------------------------------------')
    print('Clear workspaces - DONE, press "enter" to continue...')
    raw_input()