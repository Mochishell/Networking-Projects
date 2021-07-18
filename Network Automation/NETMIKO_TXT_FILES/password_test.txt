#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass
#basic script, ensure a connection can be made
#to switch 1


#read places the whole text file as one string into the variable
#splitlines splits the text file into list items based on line breaks


with open('password.txt') as f:
    devices = f.read().splitlines()
    for host in devices:
        switchX = host.split(', ')
        print (switchX)

