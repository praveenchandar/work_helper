'''
Created on 9 Aug 2019

@author: sivasp
'''


# Python script to help at OCZ
# To be run form the workspace - e.g. ...\export\software\p.sivashanmugam

import os, fnmatch, subprocess


#import local helper modules
from clear_workspace import clearWorkspaces



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