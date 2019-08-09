'''
Created on 9 Aug 2019

@author: sivasp
'''


# Python Program - To run "make cleanclean" in all the build folders in UKSFWHAWK workspace
# To be run form the workspace - e.g. ...\export\software\p.sivashanmugam

import os, fnmatch, subprocess


#import local helper modules
from clear_workspace import clearWorkspaces

# def clearWorkspaces():
#     
#     print('Clear workspaces - invokes "make cleanclean" on every build folder in /export/../psivashanmugam/')
#     script_path = os.getcwd()
# 
#     for root, dirs, files in os.walk("./../../temp/"):
#         for name in files:
#             if fnmatch.fnmatch(name, 'Makefile.ocz'):
#                 print(root)
#                 os.chdir(root)
#                 subprocess.call("make cleanclean", shell=True)
#                 os.chdir(script_path)
#     print('-----------------------------------------------------')
#     print('Clear workspaces - DONE, press "enter" to continue...')
#     raw_input()
#         
def main():
    
    usr_input = 'z'
        
    while usr_input != 'x':
        # prompt user to make a choice        
        #os.system('clear')
        print('=================================================================================')
        print('    Work helper script')
        print('=================================================================================')
        print('c - clear all the workspaces')
        print('x - exit')
        
        # get user choice
        usr_input = raw_input('Choose an option from above: ')
        if 'c' == usr_input:
            clearWorkspaces()
            
        elif 'x' == usr_input:
            # if user chooses 'x', exit the loop
            print('-----------------------------------------------------')
            break
                
        else:
            print('Invalid user input, try again dummy!!!')
        


main()